# Release Checklist

## Repository

- [ ] The default branch contains the intended tested `spoolman_plugin.py`.
- [ ] README and supporting documentation match the release.
- [ ] The README states the tested OrcaSlicer version.
- [ ] All referenced screenshots render.
- [ ] Screenshots contain no unintended private information.
- [ ] Issue templates appear under **Issues > New issue**.
- [ ] The repository contains an explicit license.
- [ ] Issues are enabled.
- [ ] Security policy is present.

## Plugin Validation

- [ ] Strict Python compilation passes.
- [ ] Full module import passes.
- [ ] Generated HTML renders.
- [ ] Embedded JavaScript syntax validation passes.
- [ ] OrcaSlicer loads the plugin after a full restart.
- [ ] Inventory refresh succeeds.
- [ ] Import Preview succeeds.
- [ ] Synchronization Preview succeeds.
- [ ] Backup and restore are tested.
- [ ] All themes are checked.
- [ ] Help and update links are checked.

## GitHub Release

- [ ] Tag follows `v1.0.x`.
- [ ] Title identifies the plugin and version.
- [ ] Release notes summarize additions, fixes, safety, and known limitations.
- [ ] Attach `spoolman_plugin.py`.
- [ ] Optionally attach a versioned archival copy.
- [ ] Mark external-testing builds as prereleases.
- [ ] Do not mark a development build as the latest stable release.

## After Publishing

- [ ] Test the Stable update channel.
- [ ] Test the Development update channel.
- [ ] Test the release page and asset links.
- [ ] Perform a clean local installation from the published asset.
- [ ] Confirm issue-template labels exist.
