# Development Plan

## Goals
- Maintain three demo targets: RoyalVNCDemo (macOS), RoyalVNCObjCDemo (macOS Obj-C), RoyalVNCiOSDemo (iOS).
- Keep the RoyalVNC submodule aligned with SDK updates.
- Validate core user flows with BDD specifications and CI automation.
- Provide a repeatable release pipeline to TestFlight.

## Primary Workflows
1. Update the RoyalVNC submodule when SDK changes are required.
2. Open `RoyalVNC.xcworkspace` and build each scheme:
   - `RoyalVNCDemo`
   - `RoyalVNCObjCDemo`
   - `RoyalVNCiOSDemo`
3. Run the BDD suite locally:
   - `python3 bdd/run_bdd.py`
4. Iterate on UI/UX in each demo app and keep feature files in sync with expected behavior.
5. For releases, use the TestFlight workflow (`testflight-release.yml`) with the required signing secrets.

## External Dependencies
- Xcode (macOS builds and signing)
- Swift toolchain (via Xcode)
- Apple signing certificates and provisioning profiles (App Store Connect)
- Git submodules (`royalvnc` SDK)
- `xcpretty` for CI build formatting
- Python 3 for BDD runner
- VHS action (for console capture GIF)
- Playwright (CI screenshot of GitHub Pages site)
- GitHub Actions runners (macOS and Ubuntu)

## CI/CD Overview
- Build workflows: `.github/workflows/build-royalvncdemo.yml`, `.github/workflows/build-royalvncobjcdemo.yml`, `.github/workflows/build-royalvnciosdemo.yml`
- BDD workflow: `.github/workflows/bdd.yml`
- TestFlight release workflow: `.github/workflows/testflight-release.yml`
- GitHub Pages screenshot workflow: `.github/workflows/pages-screenshot.yml`

## BDD Maintenance
- Add or update scenarios in `bdd/features/*.feature` when app behavior changes.
- Update step handlers in `bdd/steps.py` to reflect new scenarios.
- Re-run `python3 bdd/run_bdd.py` to validate all scenarios.
