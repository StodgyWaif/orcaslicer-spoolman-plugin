# GitHub Setup

This package is designed for `StodgyWaif/orcaslicer-spoolman-plugin`.

## One-time repository settings

1. Open the repository on GitHub.
2. Open **Settings > General**.
3. Under **Features**, enable **Issues**.
4. Add a short repository description and website link if desired.
5. Choose and add a license before broad public distribution.

## Add these files

Upload the contents of this package to the repository root while preserving folders. The `.github` folder may be hidden by some file managers, so verify that it is uploaded.

Commit message suggestion:

```text
Add project documentation and GitHub issue configuration
```

## Verify issue templates

1. Open **Issues**.
2. Select **New issue**.
3. Confirm **Bug report** and **Feature request** appear.
4. Confirm blank issues are disabled.
5. Confirm the documentation links appear below the templates.

## Prepare v1.0.72

1. Copy the confirmed plugin to the repository root as `spoolman_plugin.py`.
2. Make a second copy named `spoolman_plugin_v1.0.72.py` for the release asset.
3. Commit and push the files.
4. Open **Releases > Draft a new release**.
5. Create tag `v1.0.72` from the intended commit.
6. Use title `SpoolMan Importer v1.0.72`.
7. Add release notes from `CHANGELOG.md` plus testing cautions.
8. Attach both plugin files.
9. Select **Set as a pre-release** for external testing.
10. Publish the release.

## Update-channel verification

- Development channel should see the prerelease when it is newer than the installed build.
- Stable channel should ignore the prerelease.
- After a future stable release is published, Stable should identify that release.

## Plugin Hub

Keep GitHub Releases as the authoritative development source. Use Orca Cloud / Plugin Hub for user discovery and stable distribution after clean-install testing is complete. Follow the current OrcaSlicer plugin and Orca Cloud guidance when preparing the submission.
