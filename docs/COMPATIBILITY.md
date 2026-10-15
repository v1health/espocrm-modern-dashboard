# Compatibility and QA

Intended target: **EspoCRM 10.0.x**. Package metadata and static JS follow published extension and dashlet patterns, but **live installation and authenticated visual QA have not been run yet**.

- [ ] Install and uninstall ZIP on disposable EspoCRM 10.0.10
- [ ] Clear cache and confirm `Modern Overview (Demo)` appears in dashboard selector
- [ ] Verify view renders and no deprecated API calls are emitted
- [ ] Inspect 1440px, 768px, 390px responsive layouts and keyboard navigation
- [ ] Confirm no new external requests, no overrides to other dashboards

Official documentation:
- https://docs.espocrm.com/development/extension-packages/
- https://docs.espocrm.com/development/how-to-create-a-dashlet/
- https://docs.espocrm.com/development/modules/
- https://docs.espocrm.com/development/custom-css/

The separate V1OS production EspoCRM upgrade must follow official Docker migration requirements for EspoCRM 10; this demo is not an upgrade utility.
