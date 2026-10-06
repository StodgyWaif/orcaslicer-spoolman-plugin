# Release Checklist

## Repository

- [ ] The default branch contains the tested `spoolman_plugin.py`.
- [ ] README and supporting documentation match the release.
- [ ] Issue templates appear under **Issues > New issue**.
- [ ] The repository has an explicit license.
- [ ] Issues are enabled.

## Plugin validation

- [ ] Python compilation passes.
- [ ] Full module import passes.
- [ ] OrcaSlicer loads the plugin after a full restart.
- [ ] Inventory refresh succeeds.
- [ ] Import Preview succeeds.
- [ ] Synchronization Preview succeeds.
- [ ] Backup and restore are tested.
- [ ] All themes are checked.
- [ ] Help and update links are checked.

## GitHub release

- [ ] Tag follows `v1.0.x`.
- [ ] Title identifies the plugin and version.
- [ ] Release notes summarize additions, fixes, safety, and known limitations.
- [ ] Attach `spoolman_plugin.py`.
- [ ] Attach a versioned copy such as `spoolman_plugin_v1.0.72.py`.
- [ ] Mark external-testing builds as prereleases.
- [ ] Do not mark a development build as latest stable.

## After publishing

- [ ] Test the Stable update channel.
- [ ] Test the Development update channel.
- [ ] Test the release page and asset links.
- [ ] Perform a clean local installation from the published asset.
