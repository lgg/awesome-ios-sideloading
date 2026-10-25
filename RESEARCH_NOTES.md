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

- **Personal-account or on-device installation:** [MultiStore](https://github.com/lungustefan/MultiStore), [althea](https://github.com/vyvir/althea), [Splice](https://github.com/franklintra/splice), [ipaverse](https://github.com/bahattinkoc/ipaverse), [Scarlet](https://usescarlet.com/) (proprietary; certificate/installation method varies).
- **Renewal/self-hosted:** [Sideloop](https://github.com/filippofinke/sideloop), [AltDaemonModern](https://github.com/emp0ry/AltDaemonModern) (requires jailbreak), [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server), [omnisette-server](https://github.com/SideStore/omnisette-server).
- **IPA preparation and signing:** [altsign-cli](https://github.com/xhzq233/altsign-cli), [IPAID](https://github.com/shplash/IPAID).
- **Developers integrating JIT:** [StikJIT XCFramework](https://github.com/StikDebug/StikJIT).

### Added: early-stage projects with explicit caveats

- [BatSign](https://github.com/8yy/BatSign), [EnSign](https://github.com/cc158999/EnSign), [ForgeSign](https://github.com/Mesutcydev/ForgeSign-iOS), [SwiftIPA](https://github.com/xsxs18-dev/SwiftIPA), [Wax](https://github.com/dylldev/wax-signer).

These have repository code and descriptions of relevant features, but their security/privacy properties, app-update promises and compatibility remain **unverified** here. They are deliberately separated in the README from widely used installers.

### Considered, intentionally omitted for now

- ESign download mirrors and sites offering “permanent signing without certificates” on arbitrary new firmware — no clearly confirmed original maintainer download/source was established; avoid directing users to impersonator or untrusted IPA mirrors.
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


## Follow-up research: forums, signing APIs and source builders (2026-10-25)

This pass combined GitHub topic search (`sideloading`, `sidestore`, `altstore-source`, `anisette`), project READMEs, up-to-date public guides, and contemporary **r/sideloaded** discussions. It is a research snapshot, **not** device testing or an endorsement of every third-party project.

### Newly added projects

| Project | Rationale | Important trust/maintenance note |
| --- | --- | --- |
| [SideStore/anisette-servers](https://github.com/SideStore/anisette-servers) | Official directory of suggested Anisette services, relevant to free-account sideloading reliability | Directory inclusion and uptime should not be mistaken for a full privacy/security audit |
| [SideStore/apps.json](https://github.com/SideStore/apps.json) | First-party feed of SideStore-related releases | Distinguished from the community source |
| [CaseyCZ/iOS-Hub](https://github.com/CaseyCZ/iOS-Hub) | Active multilingual source discovery and troubleshooting, with availability checks | Its directory includes community/modified feeds; reachability does not establish app provenance |
| [ShrubHub-iOS/ShrubLibrary](https://github.com/ShrubHub-iOS/ShrubLibrary) | Large searchable source directory | GitHub repo is **not the application source code**; directory also promotes certificate offerings |
| [yazdipour/GithubStore](https://github.com/yazdipour/GithubStore) | Self-hosted AltStore source generator from selected GitHub release IPAs | Web configuration UI documented as unauthenticated |
| [yazdipour/TeleStore](https://github.com/yazdipour/TeleStore) | Self-hosted, Telegram-channel-backed AltStore source | Telegram session/credentials and legal distribution rights require care |
| [aoyn1xw/ipa-signer](https://github.com/aoyn1xw/ipa-signer) | Source-available web/API IPA signer, usable on a private host | Uploaded IPAs, certificates and profiles land on server; do not expose publicly |
| [CyberTKR/IpaSigner](https://github.com/CyberTKR/IpaSigner) | Local macOS GUI for IPA codesigning plus optional App Store Connect workflow | Early-stage Qt tool; double-check signing keys and bundle-ID changes |
| [asdfzxcvbn/pyzule-rw](https://github.com/asdfzxcvbn/pyzule-rw) | `cyan` IPA inspection/repacking/tweak injection CLI with Linux/macOS/WSL support | Not a standalone replacement for legitimate signing and provisioning |
| [username252510/Purple-Installer](https://github.com/username252510/Purple-Installer) | Web installer for Feather, Ksign and SideInstaller | **README explicitly says it transmits .p12, provisioning profile and password to the Daisuke Signer API**; front-end local storage does not make it local signing |
| [yodaluca23/Feather-Installer](https://github.com/yodaluca23/Feather-Installer) | Web-based Feather setup with certificate import | **README says certificate files and password are transmitted to the ipasign.cc signing backend** |

### Forums, documentation and communities checked

- [r/sideloaded](https://www.reddit.com/r/sideloaded/) and its [advertised Discord invite](https://discord.gg/pUHBuxYzSG): active community for recent setup problems and release feedback; user reports are anecdotes and may reflect particular firmware only.
- [SideStore GitHub organization](https://github.com/SideStore), its [official Discord](https://discord.gg/sidestore), [GitHub Discussions](https://github.com/SideStore/SideStore/discussions), and [docs](https://docs.sidestore.io/): preferred starting points for version-specific SideStore troubleshooting.
- [Apple Developer Forums — Code Signing](https://developer.apple.com/forums/topics/code-signing-topic/code-signing-topic-general): first-party Apple provisioning, entitlement and certificate diagnostics.
- [iOS Guide TrollStore documentation](https://ios.cfw.guide/installing-trollstore/): device/firmware-specific methods; compare against [TrollStore upstream](https://github.com/opa334/TrollStore).
- [GitHub sidestore topic](https://github.com/topics/sidestore), [sideloading topic](https://github.com/topics/sideloading): discovery only; tag placement and recent commits do not mean a feature works.

### Evaluated and not included in the main catalog

- [Nemesis-Surf/webipagui](https://github.com/Nemesis-Surf/webipagui) was **archived**; not presented as an actively maintained front end.
- [SignOs](https://github.com/ihateios/SignOs) and similar Feather forks claim unattended, silent signing/update workflows; insufficient independent test evidence to add yet another near-identical alternative alongside BatSign.
- [aoyn1xw/ipa-signer](https://github.com/aoyn1xw/ipa-signer) was included strictly as a **self-hosted signing server**, not a recommended public website to submit credentials to.
- [EscapeOS](https://github.com/pwnapplehat/EscapeOS) is a firmware-specific app data browser / backup utility rather than a tool for **installing or signing** IPAs; useful adjacent reference but outside the narrow main catalog.
- [Feather Installer](https://github.com/yodaluca23/Feather-Installer) and [Purple Installer](https://github.com/username252510/Purple-Installer) are included in a visibly separated risk section, **not the quick-start recommendations**.
- [ShrubLibrary](https://github.com/ShrubHub-iOS/ShrubLibrary) and [iOS Hub](https://github.com/CaseyCZ/iOS-Hub) are **source browsers**: catalogs can contain third-party modified IPAs. Linking to the directory is not endorsement of those IPAs.
- [SideKit](https://github.com/SideStore/SideKit) is described as WIP and had no recent substantial updates; it should not be mistaken for today's mainstream JIT or installer framework.

### Maintenance implications

The fastest-moving failure points remain Apple Account authentication/Anisette services, iOS **remote pairing** variants, certificate revocation, and future iOS release compatibility. Source listings need source-provenance review as well as reachability checks. A private-key upload to an untrusted signing endpoint can lead to unauthorized use of the key **even when the front-end code is open source**.

If further evidence contradicts any claim, prefer updating the entry and accompanying [COMPATIBILITY.md](COMPATIBILITY.md) with reproducible upstream links over creating another speculative entry.

## Third research pass: iOS 27 installers, modern device tools and support forums (2026-10-25)

**Goal:** go beyond broad GitHub stars and find narrow tools that actually sign, install, refresh, develop, or distribute iOS/iPadOS/tvOS apps. Upstream project documentation was used as evidence of **claimed** features; forum anecdotes were used to detect common failure modes, **not** establish universal compatibility.

### Added to the curated catalog

| Project | Reason | Important condition |
| --- | --- | --- |
| [AltLoad](https://github.com/mirazbakis/AltLoad) | On-device AltStore/SideStore/LiveContainer installer with on-device AltServer behavior | Author documents self-pairing on **iOS 27+**; **iOS 18–26 still needs a computer-created pairing file**. Its bootstrap options include shared-certificate/DNS methods, which have distinct risks. |
| [ModStaller](https://github.com/Crafttino21/ModStaller) | Linux/Windows Apple-account sideloading, JIT and optional tvOS workflows | New project with very little community validation; author labels some platform support beta. **Android-host implementation is on its roadmap, not available.** |
| [Torch](https://github.com/trollzem/torch) | macOS menu-bar signing and six-day scheduled refresh, including Apple TV | Small experimental project; modifies/ships signing tool binaries and has install scripts. Review locally before granting credentials/admin permissions. |
| [App Distribution Server](https://github.com/significa/app-distribution-server) | Host installation/QR pages for pre-signed internal IPA/APK builds | **Not** an IPA signer and not an App Store/AltStore source. Upstream docs show a default token `secret`; change it for real deployments. |
| [go-ios](https://github.com/danielpaulus/go-ios) | Device transport, pairing, app install, test automation on multiple operating systems | Installation alone does not provide a valid development signature or bypass iOS restrictions. |
| [xtool](https://github.com/xtool-org/xtool) | Linux/Windows/macOS SwiftPM toolchain with iOS development, code signing and deployment | Developer build/deploy tooling; it is not a replacement for an IPA catalog or universal compatibility claim. |
| [atv-sideload](https://github.com/Lauch2/atv-sideload) | Linux tvOS scripts with separate `plumesign` dependency and .deb-to-.ipa packaging | Upstream explicitly says its stand-alone experimental pairing code is incomplete. Not turnkey; very small project. |

### Communities and first-party support sources

- [Sideloadly official FAQ](https://sideloadly.io/faq.html) explicitly directs users to **[r/Sideloadly](https://www.reddit.com/r/Sideloadly/)**. Useful for Wi-Fi refresh-daemon problems, iTunes/Windows driver requirements and tvOS compatibility. Prefer it over non-maintainer download mirrors.
- [r/LegacyJailbreak](https://www.reddit.com/r/LegacyJailbreak/) helps with old devices, legacy jailbreak-only app installs and obsolete iOS signing behavior. This is **adjacent**, not the default no-jailbreak workflow.
- [r/jailbreak](https://www.reddit.com/r/jailbreak/) regularly discusses firmware-specific sideloading versus jailbreak/TrollStore tradeoffs; use maintainer guides to confirm exploits and available releases.
- [SideStore official issues](https://github.com/SideStore/SideStore/issues) and [SideStore organization discussions](https://github.com/orgs/SideStore/discussions) contain often more reproducible issue reports than chat/Reddit alone.
- [r/AltStore](https://www.reddit.com/r/AltStore/) and [r/sideloaded](https://www.reddit.com/r/sideloaded/) surfaced October 2026 signing/authentication discussions and contrasting personal experiences. **Claims that Apple is banning all sideloading accounts are not corroborated by these anecdotes alone.**

### October 2026 sign-in changes: what is verified

- [SideStore issue #1647](https://github.com/SideStore/SideStore/issues/1647) was opened **13 October 2026** and documents reports of `-80045` during sign-in.
- [SideStore PR #1683](https://github.com/SideStore/SideStore/pull/1683) describes client-information/Anisette and 2FA handling changes; it was **still an open PR on the date of review**. Do not present its changes as an established stable release.
- [SideStore discussion #1666](https://github.com/orgs/SideStore/discussions/1666) has community-specific temporary changes for `503`, `-80045` and `-22411`. Advice may conflict between builds.
- [AltServer macOS 27 Anisette Fix](https://github.com/kimziro/altserver-macos27-anisette-fix) documents an **unofficial and unnotarized** arm64 macOS 27 package. Its author tested USB installation but did not establish unattended refresh/remote compatibility. This is kept as a **context link**, not promoted to the primary installer list.
- [SideStore official Anisette directory](https://github.com/SideStore/anisette-servers) is the safer place to find *current* candidate servers, although listing there does not guarantee privacy.
- Some guides claim a specific hard-coded Windows/Android/Mac identity is the universal fix; server-side Apple changes make such statements fragile. We intentionally **do not pin literal client-header workarounds in the catalog**.

### Considered but not elevated as general recommendations

- [nquangdungg/LiveContainer-Extended](https://github.com/nquangdungg/LiveContainer-Extended): recent fork that largely repeats upstream's README, without clearly established distinct, independently verified capabilities. Prefer [official LiveContainer](https://github.com/LiveContainer/LiveContainer).
- [guansiriustar-prog/ios-sideload-kit](https://github.com/guansiriustar-prog/ios-sideload-kit): detailed but narrowly tested Chinese-language guide; some Anisette identity instructions risk becoming stale very quickly. More suitable as background reading than a recommended official guide.
- [pwnapplehat/EscapeOS](https://github.com/pwnapplehat/EscapeOS): actively maintained no-jailbreak app-data browser/backup utility, but still outside the core *sign/install/refresh* category.
- [fastlane/fastlane](https://github.com/fastlane/fastlane) and [codemagic-ci-cd/cli-tools](https://github.com/codemagic-ci-cd/cli-tools): reputable build/CI tools but broad mobile release automation, not specialized sideloaders.
- Projects suggesting a permanent TrollStore exploit on arbitrary new iOS builds, unverified Enterprise certificate distributors, or offering pre-signed pirated app archives: not credible/suitable for this curated list.
- **Torch**, **AltLoad**, **ModStaller** and **atv-sideload** remain **experimental** until substantial independent device testing confirms the vendor claims.

### Ongoing curation rules

Track **four different questions** independently: does a tool sign IPAs; install on the device; automatically renew provisioning; and run without desktop/host involvement? The words *on-device*, *untethered*, *no PC* and *permanent* should never be treated as synonyms. Free development signing normally retains Apple's provisioning limitations, and multiple Apple Accounts do not inherently multiply a device's three simultaneous free-app slots.

For any future compatibility PR, provide the **OS build, exact app version, signing method and observed steps**, not only the project's GitHub activity.

## Fourth research pass: official signing libraries and release verification (25 Oct 2026)

**What changed in this pass:** rather than adding another dozen near-identical IPA installers, this pass prioritizes first-party signing frameworks and resolves version-specific setup traps observed in SideStore/AltStore/LiveContainer discussions.

### Added: developer signing/authentication libraries

| Project | Why added | Boundary |
| --- | --- | --- |
| [AltSign](https://github.com/rileytestut/AltSign) | Original code-signing framework published by the AltStore developer; the [podspec](https://github.com/rileytestut/AltSign/blob/master/AltSign.podspec) describes Apple developer-account management and app re-signing | iOS framework, not a desktop installer; public root has no README |
| [SideSign](https://github.com/SideStore/SideSign) | Current **SideStore-owned** Swift framework for developer-account APIs, provisioning, nested IPA signing and certificates | Cryptographic signing is not equivalent to a supported installation path |
| [AnisetteKit](https://github.com/mahee96/AnisetteKit) | Local Anisette header generation/ADI emulation for iOS/macOS/tvOS/visionOS | Local Anisette alone does **not** remove server-side Apple authentication changes |
| [CodeSignKit](https://github.com/mahee96/CodeSignKit) | Swift Mach-O/CMS/entitlements/app-framework signer underpinning SideSign | AGPL-license and practical firmware/device compatibility need evaluation by integrators |
| [GSACryptoKit](https://github.com/mahee96/GSACryptoKit) | SRP-6a library used by SideSign to communicate with Apple GrandSlam Authentication | Low-level cryptographic library, **not** an app signer or Apple ID workaround |

The underlying implementation matters more than GitHub popularity here: [SideSign](https://github.com/SideStore/SideSign) actually names CodeSignKit, GSACryptoKit and AnisetteKit as core components. These are listed together under a clearly developer-oriented README category rather than as five consumer “installers.”

### Important changes verified against first-party releases

- **AltStore Classic 2.3.1 (21 October 2026):** the [official FAQ changelog](https://github.com/altstoreio/FAQ/blob/main/release-notes/altstore.md) says it fixes `-80045`, 2FA prompts, background refresh and Remote AltServer issues. **2.3.0 raised the minimum iOS version to 17.4**, so do not recommend Classic 2.3 for iOS 15/16.
- **SideStore 0.6.4 (9 September 2026):** [release notes](https://github.com/SideStore/SideStore/releases/tag/0.6.4) say **DO NOT USE — SIGN-IN IS BROKEN ON 0.6.4 AND BEFORE**. A subsequent [0.7.0-alpha](https://github.com/SideStore/SideStore/releases/tag/0.7.0-alpha) addresses a server-side 503 issue, but [newer open issues](https://github.com/SideStore/SideStore/issues/1652) show that later versions may still fail in certain conditions.
- **LiveContainer 3.8.0:** [official release](https://github.com/LiveContainer/LiveContainer/releases/tag/3.8.0) and [installation documentation](https://livecontainer.github.io/docs/installation) require appropriate SideStore/AltStore versions. Importantly, **Sideloadly and most online signing services are explicitly unsupported**. LiveContainer+SideStore should be installed through documented installers such as iloader/Impactor; a generic code-signing success is not enough.
- **SideInstaller 1.5.0:** [changelog](https://github.com/FrizzleM/SideInstaller/blob/main/CHANGELOG.md) reports Apple-sign-in adjustments after 12 October, not a general bypass of Apple policy. Check firmware-specific pairing requirements.
- **SideStore PR #1683:** [open on 25 October 2026](https://github.com/SideStore/SideStore/pull/1683). Do **not** treat unmerged authentication changes as released fixes.

### Additional communities investigated

- [r/SideStore](https://www.reddit.com/r/SideStore/) — narrower SideStore installation, pairing, renewal and server-error discussion; useful for detecting breakages, but comments about “bans” or fixes are not authoritative.
- [r/Trollstore](https://www.reddit.com/r/Trollstore/) — discussions include **TrollStore Lite** under jailbreak-specific conditions. They do **not** imply ordinary TrollStore is compatible with new firmware. [Example of confusion in October](https://www.reddit.com/r/Trollstore/comments/1x7d36l/trollstore_is_working_fine_on_iphone_11_ios_1862/).
- [r/sideloaded](https://www.reddit.com/r/sideloaded/) — multiple conflicting recommendations for SideStore vs AltStore vs iloader. Useful for locating symptoms, not proving universal workarounds. [Discussion example](https://www.reddit.com/r/SideStore/comments/1x23zp3/can_anyone_give_me_some_sidestore_alternatives/).
- [SideStore JIT guide](https://docs.sidestore.io/docs/advanced/jit) — warns that iOS 26/27 JIT works only in certain apps/builds. A successful JIT debugger attach does not imply an emulator will run with unrestricted JIT.

### Considered and not promoted

- [TrollStore Lite copies](https://github.com/TequilaDash/TrollStoreLite27): repositories found were small forks or potentially misleading newer-version claims, rather than a verified canonical upstream with independent compatibility evidence. Keep TrollStore Lite in the community discussion, not the “latest TrollStore for all iOS” list.
- [AltKit](https://github.com/altstoreio/AltKit): older AltServer communication package with no recent meaningful upstream activity; AltSign and SideSign are the stronger maintainer-supported code-signing references.
- General alternative app-source directories containing patched paid apps: source URLs and reachability cannot be treated as permission to redistribute third-party IPAs.
- One-off third-party “Apple ID banned” claims: do not infer a permanent ban from client error `-80045`; compare account status in Apple's legitimate account settings and upstream error reports before concluding anything.

### Conclusions

The most valuable gap in the previous version was **compatibility guidance**, not a raw project count. Fixing the version-specific AltStore/SideStore/LiveContainer information is intended to prevent broken real-world setups. All “works on iOS X” statements remain upstream claims unless accompanied by independent reproducible test evidence.

## Fifth research pass: cross-platform installers, private signers and specialized support (25 Oct 2026)

This pass searched GitHub's recently updated sideloading and IPA-signing topics, projects' **original READMEs and release metadata**, the source catalogs gathered by [iOS Hub](https://caseycz.github.io/iOS-Hub/), and discussions on [r/sideloaded](https://www.reddit.com/r/sideloaded/) and focused developer forums. We prioritized **distinct workflows**, checked whether a source provides a real distribution artifact, and separated availability/claims from verified functionality.

### New projects worth including

| Project | Evidence and why it was added | Qualification |
| --- | --- | --- |
| [IPAForge](https://github.com/IPAForge/ipaforge) | Developer ships [v0.1.0-alpha.7](https://github.com/IPAForge/ipaforge/releases/tag/v0.1.0-alpha.7) (published **21 Oct 2026**) with platform installers and Sigstore-related assets. Cross-platform free-Apple-Account setup of SideStore and LiveContainer+SideStore, IPA signing and refresh. | **Alpha**; very young project with little independent community evidence. GitHub artifacts and published signatures do not certify correct installation on every iOS version; macOS/Windows installer trust requirements vary. |
| [ryP0](https://github.com/Sami-Wali/ryP0) | Released [2.2 on 23 Oct 2026](https://github.com/Sami-Wali/ryP0/releases/tag/2.2) with `ryP0-unsigned.ipa`; browses community IPA feeds, versions, and opens supported installers. | A **catalog**, not a signer. Release asset is explicitly unsigned. Sources and individual applications must be checked for provenance, rights and security. |
| [SignTools GitHub Actions Builder](https://github.com/maxexcloo/signtools-builder) | Distinct workflow: a private SignTools service dispatches signing jobs onto macOS GitHub Actions workers over Tailscale, with persistent Apple authentication sessions. | Newly created, small **community implementation** (not an official SignTools component). Stores/reuses high-value `FASTLANE_SESSION` and repository secrets; security review required before deployment. No formal releases. |
| [IPA Signer Telegram Bot](https://github.com/lxdxrx/ipa-signer) | MIT-licensed self-hosted Telegram signing bot using `zsign`, Docker, local Telegram Bot API and OTA links. | The upstream instructions permit uploading `.p12`/`.mobileprovision` via chat. **Encryption at rest does not prevent the bot/Telegram service from receiving sensitive material**. No formal releases. |
| [Sideloadly Monitor](https://github.com/recallsangel/sideloadly-monitor) | Novel macOS launchd watcher for expiry, failed renewals, daemon health and Telegram alerts. Its own documentation states that Sideloadly's `installations.db` is opened read-only. | Community add-on, documented mostly in Traditional Chinese. Relies on **private Sideloadly database fields** that can change between proprietary releases. A daemon restart is not selective IPA redeployment. No formal releases. |

### More focused forums and knowledge sources

- **[r/jailbreakdevelopers](https://www.reddit.com/r/jailbreakdevelopers/)**: development discussion relevant to signing, entitlements, Mach-O injection, Theos, and the limits of jailbreak-dependent installations. [The Apple Wiki Developer pages](https://theapplewiki.com/wiki/Main_Page/Developer) point to this developer community and other technical resources.
- **[MacRumors iOS Jailbreaks](https://forums.macrumors.com/forums/ios-jailbreaks.105/)**: long-running site with actual recent (2026) threads but much older historical guidance; useful for **legacy cases only**, not proof that an exploit works on newer firmware.
- **[Apple Developer Forums](https://developer.apple.com/support/forums)**: first-party source for code signing, provisioning and App Store distribution questions. Its tag/topic pages provide **RSS feeds**, which could be monitored to spot platform changes.
- **[r/sideloaded discussion: state of sideloading, Sep 2026](https://www.reddit.com/r/sideloaded/comments/1wp031h/state_of_sideloading/)**: competing community recommendations for LiveContainer+SideStore via iloader and certificate services. Comments conflict about account bans; never treat anecdotes as evidence of policy.
- **[iOS Hub directory](https://caseycz.github.io/iOS-Hub/)**: regularly checks the reachability of AltStore-compatible feeds. The directory may include modified app feeds, so **online ≠ official/safe**; we did not rehost or copy its app links.
- **[GitHub sideloadly topic](https://github.com/topics/sideloadly)** and **[GitHub sideloading topic](https://github.com/topics/sideloading)**: used for discovery, with caution around unofficial projects impersonating commercial installer distribution.

### Investigated but excluded from the main list

- [laamarizineddine-max/webipagui](https://github.com/laamarizineddine-max/webipagui) — copied/promotional readme makes sweeping claims about browser-side installation on Windows, macOS, Linux and iOS 14+ but directs readers to a direct ZIP file rather than attributable release assets or documented signing infrastructure. A repo description saying “no data leaves your device” conflicts with sections implying online installers; **not reliable enough** to recommend.
- [Nemesis-Surf/webipagui](https://github.com/Nemesis-Surf/webipagui) — source project is archived (previously reviewed); not a maintained default.
- [Kasumi-dta/LemonSign](https://github.com/Kasumi-dta/LemonSign) — repository explicitly marked **discontinued**, despite recent commit activity; don't mistake “recently pushed” for “maintained”.
- [OpsNexusDev/XcodeNexus](https://github.com/OpsNexusDev/XcodeNexus) and [OpsNexusDev/NexusSign](https://github.com/OpsNexusDev/NexusSign) — surfaced in one GitHub-topic index but the canonical GitHub API returned **404** during verification; don't link to an unconfirmed repository.
- [bikram-agarwal/ObtainX](https://github.com/bikram-agarwal/ObtainX) — a project for **Android** app updates despite overlapping `sideloading` topic tags. Not iOS.
- [pwnless/AutoFLEX](https://github.com/pwnless/AutoFLEX) — relevant to authorized instrumentation but is primarily a jailbreak-adjacent debug utility, not an IPA signing/installation/update tool.
- `SideloadlyiOS/Sideloadly-Download` and similar keyword-stuffed third-party installers — do not promote as official binaries. Prefer [Sideloadly's own website](https://sideloadly.io/) and official FAQ.
- Broader communities distributing cracked commercial IPAs or shared enterprise certificates — excluded from direct download recommendations; redistribution and certificate trust are separate questions from technical sideloading.

### Follow-up verification priorities

1. Periodically re-check new alpha releases and vendor issue trackers for actual paired-device test evidence, especially **IPAForge**.
2. Monitor signing **trust boundaries**: remote server vs local device, Telegram uploads, GitHub Actions secrets, and key storage. Do not assume open-source front-end code guarantees backend confidentiality.
3. If adding a source-directory app, distinguish metadata discovery from signed IPA authenticity and installation.
4. Treat forums as **issue discovery**; confirm compatibility and security statements from maintainers, reproducible device reports, and signed release artifacts.

## Sixth research pass: AltSource automation, App Store acquisition and developer deployment (2026-10-25)

**Approach:** searched GitHub topics (`sideloading`, `sideload`, `ipa`, `altstore`), read original project READMEs, inspected current GitHub repository metadata and release assets, cross-checked [OWASP's app installation guidance](https://mas.owasp.org/MASTG/techniques/ios/MASTG-TECH-0056/) and historical [The Apple Wiki](https://theapplewiki.com/wiki/Main_Page). Used forums as *lead generation*, not proof that a sideloading method works on all firmware.

### Seven distinct additions

| Project | Evidence | Fit and limitation |
| --- | --- | --- |
| [AltGen](https://github.com/bebound/AltGen) | Maintained Python/PyPI CLI; README demonstrates GitHub releases + TOML → AltStore `apps.json` and merge support, with offline test fixtures | **AltSource generator**, no signer or OTA service; no GitHub Release assets necessary when distributed via PyPI |
| [IPATool GUI](https://github.com/a23bc/ipatool-gui) | Cross-platform Electron wrapper for [ipatool](https://github.com/majd/ipatool). Published [v0.2.0 on 21 Oct 2026](https://github.com/a23bc/ipatool-gui/releases/tag/v0.2.0) with Windows/macOS/Linux release packages. | App Store downloading and account management, **not IPA signing or DRM removal**. macOS builds are ad-hoc signed/not notarized; install restrictions apply |
| [Appium resigner](https://github.com/appium/resigner) | Go tool for local IPA/.app inspection and re-signing in Appium/WebDriverAgent workflows. [v0.3.1 release](https://github.com/appium/resigner/releases/tag/v0.3.1) includes Windows/macOS/Linux assets. | Upstream says **do not use for production app signing**. Correct provisioning and private-key handling still necessary |
| [iOS Developer Toolkit](https://github.com/hideouts-io/iOS-Developer-Toolkit) | macOS PySide6 workbench wrapping pymobiledevice3 with DDI mounting, device logs/backup, app inventory, IPA installation. [v0.3.4](https://github.com/hideouts-io/iOS-Developer-Toolkit/releases/tag/v0.3.4) has Mac builds and SHA256 manifests. | Device development & diagnostics; **does not sign apps, bypass sandboxes or jailbreak**. More broad functionality than a single IPA installer |
| [KeepAlive](https://github.com/oli-zr/keepalive) | [v1.2.4 published 19 Oct 2026](https://github.com/oli-zr/keepalive/releases/tag/v1.2.4); macOS menu-bar task rebuilding Xcode applications and installing before 7-day free-account profile expiry. | **Only Xcode source projects you own**, not automatic refresh of arbitrary prebuilt IPAs; needs local Xcode and paired iPhone |
| [SignTools Builder (official)](https://github.com/SignTools/SignTools-Builder) | First-party SignTools project, [v1.1.20 release](https://github.com/SignTools/SignTools-Builder/releases/tag/v1.1.20). Mac as self-hosted signing worker rather than a CI provider. | Original README explicitly warns: **no built-in TLS** and network-level access can enable arbitrary commands. Strong isolation required, preferably dedicated Mac |
| [IpaDownloadTool](https://github.com/SmileZXLee/IpaDownloadTool) | Established MIT-licensed iOS tool for resolving OTA `itms-services` manifests and fetching development/enterprise IPA archives, with updated repository activity in October. | Useful **only for authorized distribution/inspection**; downloading a signed enterprise archive is not authorization to install/redistribute; it cannot remove Apple DRM |

### More research resources

- [OWASP MASTG: Installing Apps](https://mas.owasp.org/MASTG/techniques/ios/MASTG-TECH-0056/) explains `installd`, signatures and official versus jailbreak-specific installation options. It is **security testing documentation**, not an app-download platform.
- [The Apple Wiki](https://theapplewiki.com/wiki/Main_Page) contains historical Apple/Jailbreak internals, signing and developer-component discussion. Some pages explicitly describe firmware-era APIs deprecated years ago; **never generalize legacy code-signature bypass recipes to current iOS**.
- [r/sideloaded](https://www.reddit.com/r/sideloaded/), [r/jailbreakdevelopers](https://www.reddit.com/r/jailbreakdevelopers/) and [Apple Developer Forums](https://developer.apple.com/forums/) remain useful for spotting failure patterns, but unverified forum reports and single-device anecdotes cannot override actual release documentation.

### Considered but not added

- [pdx15/ipatool-webGUI](https://github.com/pdx15/ipatool-webGUI): useful Russian/English GUI and legacy App Store catalog, but its README describes Windows builds and simultaneously says authentication requires **macOS + cgo**. Needs clarified cross-platform evidence before adding next to IPATool GUI; FairPlay-encrypted archives remain tied to the acquiring account.
- [RinTaigyoku/RhineSign](https://github.com/RinTaigyoku/RhineSign): very new Windows USB/Apple Account signer, initial release created 24 October 2026 with **limited independent history**; notably does not yet support IPAs containing App Extensions. Monitor for more device testing rather than presenting as proven.
- [black-night-heron/iloader-export](https://github.com/black-night-heron/iloader-export): thin unofficial exporter of iLoader private signing certificate and key. Distinct use case but **high credential exposure risk** and very limited adoption; better treated as a security-relevant reference.
- [oli-zr/keepalive](https://github.com/oli-zr/keepalive) **is not equivalent** to [Torch](https://github.com/trollzem/torch), [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) or [Sideloop](https://github.com/filippofinke/sideloop): their update/renewal models and host prerequisites are materially different.
- [omeritzics/Updatium](https://github.com/omeritzics/Updatium): **Android APK** updater surfaced by a generic sideloading search, not iOS.
- [kelvinBen/AppInfoScanner](https://github.com/kelvinBen/AppInfoScanner): valuable general red-team asset recon, but neither IPA installation nor signing pipeline-specific.
- Broad app markets, pre-signed certificate shares, unauthorized modified IPAs and “permanent signing” claims on all firmware: don't promote without original provenance and reproducible device requirements.

### Compatibility lesson

A tool can **download an .ipa** and still have no means to sign or install it. An App Store-downloaded IPA may contain FairPlay-encrypted executables tied to the purchasing Apple account. A binary fetched from `itms-services` might already be signed but is subject to its provisioning profile, allowed UDIDs, expiry and licensing. A source JSON generator only compiles **metadata URLs**, not a verified build. A self-hosted signer must be treated as a privileged service, especially where user-provided signing keys or Apple sessions are involved.

## Seventh research pass: tvOS, visionOS and offloaded app restoration (25 October 2026)

**Motivation:** the catalog previously centered on iPhone sideload installers, leaving real coverage gaps for **Apple TV 4K**, **Vision Pro JIT**, **restoring an offloaded application**, and **inspecting IPA signatures before use**. Discovery combined GitHub's active `sideloading`, `sideload`, `ipa`, and `tvos` topics, original developer READMEs and GitHub Releases, and recent [October 2026 Apple TV sideloading community discussion](https://www.reddit.com/r/sideloaded/comments/1x1s4js/apple_tv_sideloading_scene_in_2026/).

### Eight projects selected

| Project | Original evidence | Caveat / distinct reason for including |
| --- | --- | --- |
| [Apparition](https://github.com/illixion/Apparition) | Newly published [v0.3.2 on 24 October 2026](https://github.com/illixion/Apparition/releases/tag/v0.3.2), with IPA assets for iOS, tvOS and visionOS plus Linux installer. README explains desktop bootstrap, on-device refresh via LocalDevVPN/companion, and an attach-and-maintain-debugger approach to JIT. | Ambitious **early-stage** project with very little independent review. Actual JIT applicability depends on platform, OS, app and hardware. On-device refresh **still requires first pairing/bootstrap** and appropriate networking permissions. |
| [Lodestar](https://github.com/asroya/lodestar) | [v1.0.0 on 15 October 2026](https://github.com/asroya/lodestar/releases/tag/v1.0.0), source and Mac app. Maintainer explicitly distinguishes physical-device verification of USB iPhone and already-paired tvOS 27 Apple TV 4K installation from untested **first pairing**, SMS 2FA and some refresh flows. | Native Apple Silicon macOS signing app. **No background auto-refresh**, unlike Torch/AltKeeper/tvsign; refresh is one click. Very small project but transparent test matrix. |
| [tvsign](https://github.com/esalwey/tvsign) | [v1.0.1 published 16 October 2026](https://github.com/esalwey/tvsign/releases/tag/v1.0.1), Windows app and Linux/Docker Dockerfile instructions. README covers NAS/Raspberry Pi hosting, local Bonjour pairing, device-specific renewal before seven days. | Distinct **Windows or self-hosted Docker tvOS signer** with hosted renewal; Docker Desktop on Windows/macOS is specifically not the documented supported path. Always-on host, mDNS/VLAN routing and admin-surface security matter. |
| [Catapult](https://github.com/byrvr/catapult) | [v0.4.2 on 18 September 2026](https://github.com/byrvr/catapult/releases/tag/v0.4.2), public macOS DMG and detailed architecture docs. SwiftUI desktop UI plus local Python server, periodic refresh and optional **client-side encrypted IPA vault** synced across the user's Macs. | Unlike Lodestar, it claims **automatic refresh**, and unlike basic signers includes encrypted sync. No third-party device/crypto audit was performed. Keep sync disabled unless its key management is understood. |
| [AppRestore](https://github.com/J3ckJ/AppRestore) | [v0.4.0 on 13 October 2026](https://github.com/J3ckJ/AppRestore/releases/tag/v0.4.0): Mac/Windows GUI, CLI scripts, SHA256SUMS. App-specific restore of previously purchased/downloaded **offloaded or removed** apps through device restore or authorized IPA fallback. | Distinct from developer-app sideloading: cannot bypass Apple's FairPlay DRM or obtain apps not in the account's purchase history. Can be especially useful when an app is no longer listed in a regional App Store. |
| [AppInspect](https://github.com/iCrazeiOS/AppInspect) | Active Electron/TypeScript IPA/DEB/Mach-O static-analysis project with entitlement, Info.plist, Swift/ObjC strings/symbols and basic security checks. | **Offline static inspection** rather than signing or installation; no published GitHub releases were returned during this research. Static flags do not prove malware or a clean app. |
| [SignTools-CI](https://github.com/SignTools/SignTools-CI) | **First-party** SignTools GitHub Actions / Semaphore build template. Its own README warns that **SignTools 3.0 dropped support for free developer accounts**. | Complements the first-party standalone SignTools Builder and community Tailscale Actions worker already in the list. Sign job workers need private repositories, scoped CI tokens and safe storage of certificates. |
| [TapOk IPA Tools](https://github.com/TapOk38/tapok-ipa-tools) | [suite-v1.0.0-beta.5 on 13 October 2026](https://github.com/TapOk38/tapok-ipa-tools/releases/tag/suite-v1.0.0-beta.5), with Windows downloader, Windows USB IPA installer and **Android USB installer APK**. Documentation available in Russian and English. | This is **beta**, has extremely limited independent validation, and **installation is not signature bypass**. Notable as an Android-host workflow that the ModStaller roadmap has not yet implemented. |

### Narrower communities and supporting context

- [r/iosdev](https://www.reddit.com/r/iosdev/) — mainstream developer discussion where provisioning profiles, certificates, builds and legitimate distribution are covered in more detail than generic sideload forums. [Example code-signing discussion](https://www.reddit.com/r/iosdev/comments/1bfm7as).
- [r/visionosdev](https://www.reddit.com/r/visionosdev/) — specialized visionOS development subreddit; surfaced via an [overview of Vision Pro developer subreddits](https://www.reddit.com/r/VisionPro/comments/14hotsm). Check current activity before relying on it.
- [r/sideloaded: Apple TV sideloading scene in 2026](https://www.reddit.com/r/sideloaded/comments/1x1s4js/apple_tv_sideloading_scene_in_2026/) — lively October 9 tvOS sharing/compatibility discussion. Some replies promote certificate sellers and redistributed app archives; the user reports are **not** endorsements or reproducible tests.
- [r/sideloaded: Apple TV OTA experiences](https://www.reddit.com/r/sideloaded/comments/1q9yfhr/sideloading_appletv_2026/) — self-hosted atvloadly experiences on tvOS, useful for identifying mDNS/pairing questions.
- [Apple Developer Forums: code signing](https://developer.apple.com/forums/topics/code-signing-topic/code-signing-topic-general) remains the primary reference when a developer certificate, profile or entitlement is unexpectedly rejected; community screenshots alone cannot establish an Apple-wide account block.

### Exclusions and open questions

- [FrizzleM/BreakFree](https://github.com/FrizzleM/BreakFree) — a shared certificate / DNS-blocking shortcut. Distinct workflow, but reliance on *third-party public certificates*, revocations and opaque DNS profile changes makes it unsuitable to recommend alongside self-signed tools.
- [pdx15/ipatool-webGUI](https://github.com/pdx15/ipatool-webGUI) — README simultaneously advertises Windows GUI builds and documents **macOS-only cgo-based App Store authentication**. This deserves hands-on clarity before listing as a fully cross-platform downloader.
- [RinTaigyoku/RhineSign](https://github.com/RinTaigyoku/RhineSign) — Windows personal-account signer created 24 October with limited validation and documented **no App Extension support**. Monitor rather than suggest as proven.
- [byrvr/catapult](https://github.com/byrvr/catapult) and [illixion/Apparition](https://github.com/illixion/Apparition) include cloud or on-device workflows substantially more complicated than their feature summaries; only maintainer-provided facts were verified.
- [gkuhtov/GeraKStore](https://github.com/gkuhtov/GeraKStore) and [SimoGHcoder/iosrepo](https://github.com/SimoGHcoder/iosrepo) — personal app feed/catalogs with comparatively little distinct tooling value. A hosted IPA list isn't proof of application provenance.
- [QuarkSources/quarksources.github.io](https://github.com/QuarkSources/quarksources.github.io) — GitHub repository archived; not a recommended current source.
- [omeritzics/Updatium](https://github.com/omeritzics/Updatium) / [sunic007/tvinstaller](https://github.com/sunic007/tvinstaller) / [wylandplex/zappctl](https://github.com/wylandplex/zappctl) — Android APK, Samsung Tizen and Suunto BLE app installers, respectively; name/topic matches are not enough for an iOS list.

### Next practical quality improvements

The repo already validates **local Markdown links and duplicate main entries** on PRs. It should additionally introduce an **external-link liveness workflow** with HTTP rate limits, redirects, exception reports and checks against verified GitHub repository metadata. This is distinct from **security verification**: an HTTP 200 response does not attest IPA authenticity, device compatibility or license rights.

Maintain separate evidence levels in any future compatibility report: **published artifact**, **maintainer-reported device test**, **independent reproduced test**, and **unverified claim**. Update release versions and minimum OS references as new builds appear rather than leaving 2026 snapshots as evergreen facts.

## Eighth research pass: SideStore-derived apps, Linux packaging and beta channels (25 October 2026)

**Discovery scope:** active GitHub topics `altstore`, `sidestore`, `altstore-source`, `ipa-signing`, `sideloading`; recent October 2026 developer reports in [r/SideStore](https://www.reddit.com/r/SideStore/) and [r/sideloaded](https://www.reddit.com/r/sideloaded/), and original upstream project READMEs, metadata and **published release assets**. The goal was to find distinct functionality while avoiding falsely declaring every freshly pushed Feather or SideStore fork safe.

### Curated additions and evidence

| New project | Why this is worth listing | Limits and evidence |
| --- | --- | --- |
| [SideKick](https://github.com/huzaifah1530-bot/SideKick) | Extends SideStore UX with a managed IPA library, GitHub Releases and **GitHub Actions artifact** update tracking, multiple named GitHub tokens, explicit LiveContainer guest app listings. Distinct from pure installer forks. | [v0.10.0 (20 October 2026)](https://github.com/huzaifah1530-bot/SideKick/releases/tag/v0.10.0) is a **pre-release**, ships `SideKick.ipa` and a corresponding-source archive. README expressly says core sign/install/refresh is supported but advanced feature integration and device test coverage are incomplete. It reuses SideStore's AGPL implementation. |
| [DenizSigner](https://github.com/LaFAirs/DenizSigner) | Windows-only Rust/Tauri tool presenting Apple Account signing, USB installation, pairing management, and optional SideStore/LiveContainer bootstrap. Privacy-oriented design includes network allowlist and Windows local credentials. | [v0.1.0 (24 September 2026)](https://github.com/LaFAirs/DenizSigner/releases/tag/v0.1.0) publishes MSI, installer EXE, portable EXE. Real-device screenshots are explicitly unfinished; low adoption, **not independently security audited**. Apple services and a chosen Anisette server are external dependencies. |
| [SignOs](https://github.com/ihateios/SignOs) | Public **Feather-derived** IPA signer exploring a unified app catalog, cloning, certificate management and scheduled updates. | [v1.0.0 (6 September 2026)](https://github.com/ihateios/SignOs/releases/tag/v1.0.0) has an IPA. Upstream asserts silently automated app installs and 7-day renewal; these are **not independently verified**, can be constrained by iOS background execution and system prompts, and should not be promoted as general jailbreak-free bypasses. |
| [iloader Fedora COPR packaging](https://github.com/anudeepd/iloader-fedora-copr-ci) | Distinct installation *distribution* for Fedora x86_64, with scheduled upstream release checks and recorded SHA256 checking when packaging the established [iloader](https://github.com/nab138/iloader). | Not an official Fedora package and the maintainer **repackages the upstream RPM binary** instead of compiling from source. Review the linked [COPR repo](https://copr.fedorainfracloud.org/coprs/anudeepd/iloader/) and Fedora third-party repository trust implications. |
| [Awesome TestFlight Links](https://github.com/pluwen/awesome-testflight-link) | Highly maintained catalog of official Apple TestFlight public betas across iPhone/iPad, Apple TV, Mac and Vision Pro. Covers **authorized developer-distributed beta software** not previously documented in the catalog. | Not an IPA signer, developer certificate solution, sideload bypass, or guarantee of open invitation slots. The per-app status displayed in the README can expire between checks; use Apple's official TestFlight app to join valid invitations. |

### Focused October issues and communities

- [r/sideloading](https://www.reddit.com/r/sideloading/) — distinct from r/sideloaded; [22 Oct reports](https://www.reddit.com/r/sideloading/comments/1xcsy5q/fix_for_error_80045_80046_and_app_closing_when/) distinguish `-80045`, `-80046`, and crashes after sign-in on SideStore. One-off Anisette reset instructions are not universal.
- [r/SideStore: October 12 authentication thread](https://www.reddit.com/r/SideStore/comments/1x4ag7b/apple_account_logins_no_longer_working_sidestore/) — contains a multi-day history including iloader repair reports and contradictory Windows/Android/Mac Anisette workarounds. Community comments are *diagnostic leads*, not a standardized release process.
- [r/sideloaded: October 21 login thread](https://www.reddit.com/r/sideloaded/comments/1xbht4m/sidestore_sign_in_not_working/) — multiple affected installers and changing Apple login behavior; platform, build and account state differ among reports.
- [r/AltStore: October 22 discussion](https://www.reddit.com/r/AltStore/comments/1xcxi2u/please_explain_what_is_happening/) — users explicitly challenged the claim that `-80045` proves an account ban; reinforces our requirement not to conflate transport/client errors with confirmed Apple account penalties.
- [SideStore PR #1683](https://github.com/SideStore/SideStore/pull/1683) was **still open on 25 Oct 2026** and therefore cannot be described as a shipped stable login fix.

### Looked at but held back

- [striker91n/SideKick](https://github.com/striker91n/SideKick) is merely a GitHub fork of the selected SideKick upstream without proven distinctive capability.
- [tabbieelectric8182/SignOs](https://github.com/tabbieelectric8182/SignOs) has minimal independent identity or detailed test history versus [ihateios/SignOs](https://github.com/ihateios/SignOs); avoid a near-duplicate.
- [nquangdungg/LiveContainer-Extended](https://github.com/nquangdungg/LiveContainer-Extended) remains questionable as a separate entry until concrete, reproducible differences from [official LiveContainer](https://github.com/LiveContainer/LiveContainer) are documented.
- [RipeStore/altmaker](https://github.com/RipeStore/altmaker) is in the maintainer's *testing phase*, with limited proven features; [AltGen](https://github.com/bebound/AltGen) and [GithubStore](https://github.com/yazdipour/GithubStore) cover verified source-generation scenarios.
- [LaFAirs/DenizSigner](https://github.com/LaFAirs/DenizSigner) and [huzaifah1530-bot/SideKick](https://github.com/huzaifah1530-bot/SideKick) were added as early-stage projects, **not endorsed for primary Apple Accounts**.
- [pluwen/awesome-testflight-link](https://github.com/pluwen/awesome-testflight-link) is an adjacent **official Apple beta-distribution discovery resource**; its availability labels are not guarantees of invitation status.
- [SignTools GitHub Actions Builder](https://github.com/maxexcloo/signtools-builder) and [anudeepd/iloader-fedora-copr-ci](https://github.com/anudeepd/iloader-fedora-copr-ci) are separate from upstream first-party release channels and should be clearly labelled.

### Maintenance observations

Catalog quality is now limited less by number of GitHub links than by evidence freshness. Future updates should record **first-party release date**, **actual artifact presence**, **trust boundary** (local signing vs third-party Anisette vs uploaded certificates), **firmware prerequisites**, and **provenance/reproducible on-device tests**. Optional full URL liveness checks must distinguish GitHub rate limits, temporary 403s and anti-bot pages from deleted repositories.

Back to [README](README.md).
