# Modern Dashboard for EspoCRM

[![Validate Demo Extension](https://github.com/v1health/espocrm-modern-dashboard/actions/workflows/validate.yml/badge.svg)](https://github.com/v1health/espocrm-modern-dashboard/actions/workflows/validate.yml)

**An open-source, responsive demo dashlet for EspoCRM.**

Created by **[V1 Health](https://v1health.ro/)** · [Science & quality](https://v1health.ro/pages/stiinta).

> **Research preview v0.1.0** — metadata follows official EspoCRM extension conventions, but installation on EspoCRM 10.0.10 has **not** yet been verified in a live sandbox. Do not install on production before staging QA.

### What you get
A compact, modern operations overview with **four KPI cards, a weekly activity chart, Action Center and sample project table**. All values are explicitly **fictional**. The extension has no API calls, cron jobs, DB migrations, external scripts or credential handling. CSS is scoped under `.v1md-root`.

### Install (isolated staging only)
1. Build the extension ZIP: `python scripts/build.py`.
2. In EspoCRM: **Administration → Extensions → Upload → Install**.
3. Clear cache and choose **Add Dashlet → Modern Overview (Demo)**.
4. Test viewport widths 1440/768/390, browser console, uninstall and permissions before production use.

### Compatibility
Manifest targets EspoCRM **>=10.0.0 <11.0.0**. This target range is **not** a verified compatibility claim. For v9 and earlier no support claim is made. [Testing checklist](docs/COMPATIBILITY.md).

### Layout
- [Installable extension source](extension/)
- [Browser preview](preview/index.html)
- [Security model](SECURITY.md)
- [Build script](scripts/build.py)
- [MIT license](LICENSE)

**Source is original and standalone.** No data, backend code, credentials, configuration, or commit history from the V1OS production CRM is part of this repository.

Maintained by **[V1 Health](https://v1health.ro/)**. This community project is not affiliated with or endorsed by EspoCRM.
