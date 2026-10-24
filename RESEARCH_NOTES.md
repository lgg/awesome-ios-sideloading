# Research notes — iOS sideloading ecosystem

**Reviewed:** 2026-10-25 · **Scope:** installers, certificate signing, renewal infrastructure, app packaging, device pairing, JIT support, and reputable app-source tooling.

This file records **why** projects were included or excluded. It is not a security audit or a claim that every advertised feature was tested. For feature-level details, follow each project’s primary README, release notes, and [compatibility table](COMPATIBILITY.md).

## Review of 0xdad0/awesome-iOS-security-tools

Reference: **[0xdad0/awesome-iOS-security-tools](https://github.com/0xdad0/awesome-iOS-security-tools)**, a broad security/reverse-engineering list. Its purpose is different: most tools there are useful for *analyzing* iOS apps, rather than *signing, installing or refreshing* IPAs.

### Added from that list

| Upstream project | Why it belongs | Where |
| --- | --- | --- |
| [node-applesign](https://github.com/nowsecure/node-applesign) | IPA re-signing CLI/module | Signing and IPA tooling |
| [ipa-extract-info](https://github.com/nowsecure/ipa-extract-info) | IPA Info.plist metadata inspection | IPA inspection and authorized research |
| [ios-deploy](https://github.com/ios-control/ios-deploy) | macOS CLI to install/debug apps on devices | Desktop installers and setup |
| [libplist](https://github.com/libimobiledevice/libplist) | Apple property-list parsing used by signing/IPA tools | Device pairing and developer infrastructure |
| [libusbmuxd](https://github.com/libimobiledevice/libusbmuxd) | USB mux client library | Device pairing and developer infrastructure |
| [usbmuxd](https://github.com/libimobiledevice/usbmuxd) | USB multiplexing daemon used by device tools | Device pairing and developer infrastructure |
| [frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump) | Adjacent capability for **authorized** IPA extraction on jailbroken devices | IPA inspection and authorized research |

### Already listed

- [ipatool](https://github.com/majd/ipatool) — App Store package downloads.
- [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) and [ideviceinstaller](https://github.com/libimobiledevice/ideviceinstaller) — device transport and app management.
- [iOS App Signer](https://github.com/DanTheMan827/ios-app-signer) — IPA re-signing GUI.
- Maintained [Procursus ldid](https://github.com/ProcursusTeam/ldid) is already preferred over the original list's older [xerub/ldid](https://github.com/xerub/ldid) fork.

### Evaluated but not imported

| Project or group | Decision |
| --- | --- |
| [ipainstaller](https://github.com/autopear/ipainstaller) and legacy [Cydia Impactor](https://www.cydiaimpactor.com/) | Historical relevance, but too outdated as modern recommended installation paths; consider a dedicated legacy section if needed |
| [bagbak](https://github.com/ChiChou/bagbak) | Its own description marks it **deprecated**; a different authorized IPA extraction project is listed |
| [itms-services](https://www.npmjs.com/package/itms-services) | Niche OTA manifest-download helper; needs a stronger maintenance/security case before inclusion |
| [ipsw](https://github.com/blacktop/ipsw), [Clutch](https://github.com/KJCracks/Clutch), [Keychain-Dumper](https://github.com/ptoomey3/Keychain-Dumper), [idb](https://github.com/facebook/idb) | General firmware reverse engineering, encryption dumping or device/security automation, not sideloading-specific enough |
| checkra1n, unc0ver, palera1n and AppSync | General jailbreak or jailbreak-specific injection ecosystem; not an alternative to normal IPA signing. A narrowly focused jailbreak signing tool may qualify if maintained and clearly described |
| Frida/Objection/MobSF/RE/forensics/CTF material | Generic pentest and security research; belongs in the source awesome list, not duplicated here |
| Archived forks, fake “TrollStore on any iOS” claims | Avoid impersonators and misleading compatibility claims |

**Key distinction:** a decrypted IPA extractor, a certificate signer, an installer, a full jailbreak and a security scanner are **not interchangeable**. We only keep adjacent tooling when it contributes directly to understanding or managing the sideloading workflow.

## Additional 2026 ecosystem research

### Added: usable tools and supporting infrastructure

- **Personal-account or on-device installation:** [MultiStore](https://github.com/lungustefan/MultiStore), [althea](https://github.com/vyvir/althea), [Splice](https://github.com/franklintra/splice), [ipaverse](https://github.com/bahattinkoc/ipaverse).
- **Renewal/self-hosted:** [Sideloop](https://github.com/filippofinke/sideloop), [AltDaemonModern](https://github.com/emp0ry/AltDaemonModern) (requires jailbreak), [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server), [omnisette-server](https://github.com/SideStore/omnisette-server).
- **IPA preparation and signing:** [altsign-cli](https://github.com/xhzq233/altsign-cli), [IPAID](https://github.com/shplash/IPAID).
- **Developers integrating JIT:** [StikJIT XCFramework](https://github.com/StikDebug/StikJIT).

### Added: early-stage projects with explicit caveats

- [BatSign](https://github.com/8yy/BatSign), [EnSign](https://github.com/cc158999/EnSign), [ForgeSign](https://github.com/Mesutcydev/ForgeSign-iOS), [SwiftIPA](https://github.com/xsxs18-dev/SwiftIPA), [Wax](https://github.com/dylldev/wax-signer).

These have repository code and descriptions of relevant features, but their security/privacy properties, app-update promises and compatibility remain **unverified** here. They are deliberately separated in the README from widely used installers.

### Considered, intentionally omitted for now

- [BreakFree](https://github.com/FrizzleM/BreakFree) — its README explicitly describes **leaked enterprise certificates and blocking Apple verification domains**. We do not recommend this as a durable or low-risk method.
- [FlareStore](https://flarestore.app/) — commercial certificate storefront / web signer with a requirement to upload sensitive signing assets in some workflows. Possible future entry if its on-device application, identity handling, and independent trust evidence justify inclusion, with a conspicuous warning.
- [misaka26](https://github.com/straight-tamago/misaka26) — broad customization utility that includes TrollStore installation on some firmware, but is not primarily a sideloading tool.
- [TrollStar](https://github.com/34306/TrollStar) and other historical TrollStore installers — official [TrollStore](https://github.com/opa334/TrollStore) firmware-specific installation guides are a better primary index.
- Generic repositories of modified or commercial IPAs, certificate distribution mirrors, and misleading “TrollStore 3 for iOS 26” lookalikes — outside scope, untrusted, or potentially unauthorized.
- Android sideloading projects accidentally returned by GitHub’s `sideloading` topic search — not relevant.

## Verification approach

1. Used the original upstream list and current GitHub topic/repository discovery to identify candidates.
2. Resolved candidate repository URLs and checked their canonical owners, descriptions, archived status, and most recent repository activity where available.
3. Read primary README documentation for important new methods, especially multi-account refresh, self-hosted provisioning, and certificate handling.
4. Compared against the existing README to prevent duplicate primary project entries.
5. Used the [SideStore JIT documentation](https://docs.sidestore.io/docs/advanced/jit), [TrollStore firmware support](https://github.com/opa334/TrollStore), and [Apple alternative-distribution rules](https://support.apple.com/en-ie/118110) for version-sensitive context.

**Limits:** `pushed_at` and GitHub stars indicate activity/community interest, **not successful installs** or trustworthy code. No full code audit or on-device compatibility certification has been performed across these projects. There may be other worthwhile tools not yet discovered.

## Keep this list fresh

Future pull requests should prioritize updates to support tables and maintainer status over simply increasing the number of links. Prefer first-party compatibility evidence; flag uncertain claims. Run `python3 scripts/validate_catalog.py` before merging.

Back to [README](README.md).
