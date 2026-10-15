from pathlib import Path
import json, re, shutil, subprocess, unittest, zipfile

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / "extension/files"
BACK = MOD / "custom/Espo/Modules/V1ModernDashboard/Resources"
FRONT = MOD / "client/custom/modules/v1-modern-dashboard"

class StaticChecks(unittest.TestCase):
    def test_manifest(self):
        m = json.loads((ROOT / "extension/manifest.json").read_text())
        self.assertEqual(m["version"], "0.1.0")
        self.assertEqual(m["acceptableVersions"], [">=10.0.0 <11.0.0"])

    def test_metadata(self):
        client = json.loads((BACK / "metadata/app/client.json").read_text())
        dashlet = json.loads((BACK / "metadata/dashlets/V1ModernOverview.json").read_text())
        self.assertEqual(client["cssList"][0], "__APPEND__")
        self.assertTrue((MOD / client["cssList"][1]).exists())
        self.assertEqual(dashlet["view"], "module/v1-modern-dashboard/views/dashlets/overview")
        self.assertTrue((FRONT / "src/views/dashlets/overview.js").exists())

    def test_static_only(self):
        js = (FRONT / "src/views/dashlets/overview.js").read_text()
        self.assertIn("DEMO DATA", js)
        self.assertIn("https://v1health.ro/", js)
        self.assertNotRegex(js, r"\\b(fetch|XMLHttpRequest|Espo\\.Ajax|localStorage|sessionStorage)\\b")

    def test_no_secrets(self):
        secret = re.compile(r"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{25,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY")
        for p in ROOT.rglob("*"):
            if p.is_file() and p.suffix in {".py", ".js", ".css", ".json", ".md", ".html"}:
                self.assertNotRegex(p.read_text(encoding="utf-8"), secret, str(p))
        self.assertFalse((ROOT / ".env").exists())

    def test_build(self):
        subprocess.run(["python", str(ROOT / "scripts/build.py")], check=True, capture_output=True)
        with zipfile.ZipFile(ROOT / "dist/v1-modern-dashboard-0.1.0.zip") as z:
            self.assertIn("manifest.json", z.namelist())
            self.assertIn("files/custom/Espo/Modules/V1ModernDashboard/Resources/metadata/dashlets/V1ModernOverview.json", z.namelist())
            self.assertTrue(all(".." not in name.split("/") for name in z.namelist()))

    def test_js_syntax(self):
        if not shutil.which("node"):
            self.skipTest("Node.js not installed")
        f = FRONT / "src/views/dashlets/overview.js"
        proc = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)

if __name__ == "__main__":
    unittest.main()
