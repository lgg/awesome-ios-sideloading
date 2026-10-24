# Awesome iOS Sideloading

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated list of tools and resources for sideloading apps on iOS, iPadOS, and tvOS: installers, signing utilities, self-hosted servers, JIT, pairing tools, and app sources.

**[Find a tool](#start-here)** · **[Projects](#projects)** · **[Compatibility](COMPATIBILITY.md)** · **[Contribute](CONTRIBUTING.md)**

This list focuses on **the sideloading ecosystem itself**, not collections of modified or pirated IPA files. Links prefer original developers and primary documentation. Inclusion is **not an endorsement or a security audit**. Project availability, signing restrictions, iOS support, and maintenance can change.

_Last catalog review: 2026-10-25. Project descriptions are based on upstream documentation unless stated otherwise; entries are **not independently security-audited or tested on all physical devices**._

## Contents

- [Start here](#start-here)
- [Projects](#projects)
  - [App installers and managers](#app-installers-and-managers)
  - [Emerging on-device signers](#emerging-on-device-signers)
  - [Hosted signing front ends](#hosted-signing-front-ends)
  - [Desktop installers and setup](#desktop-installers-and-setup)
  - [Refresh, AltServer, and self-hosting](#refresh-altserver-and-self-hosting)
  - [Signing and IPA tooling](#signing-and-ipa-tooling)
  - [Signing and authentication libraries](#signing-and-authentication-libraries)
  - [IPA inspection and authorized research](#ipa-inspection-and-authorized-research)
  - [TrollStore ecosystem](#trollstore-ecosystem)
  - [JIT and local networking](#jit-and-local-networking)
  - [Device pairing and developer infrastructure](#device-pairing-and-developer-infrastructure)
  - [App sources and discovery](#app-sources-and-discovery)
  - [Self-hosted distribution and app sources](#self-hosted-distribution-and-app-sources)
  - [Projects in development](#projects-in-development)
  - [Apple TV and legacy devices](#apple-tv-and-legacy-devices)
- [Region-specific marketplaces](#region-specific-marketplaces)
- [Documentation](#documentation)
- [Communities and support](#communities-and-support)
- [Research notes and scope](#research-notes-and-scope)
- [Safety and limitations](#safety-and-limitations)
- [Contributing](#contributing)

## Start here

| I want to… | Good starting points |
| --- | --- |
| Install IPAs using a free Apple Account | [AltStore Classic](https://github.com/altstoreio/AltStore), [SideStore](https://github.com/SideStore/SideStore), [Sideloadly](https://sideloadly.io/) |
| Refresh apps without relying on a desktop session | [SideStore](https://github.com/SideStore/SideStore), [MultiStore](https://github.com/lungustefan/MultiStore), [AltStore Classic + Remote AltServer](https://github.com/altstoreio/AltStore/releases), [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) (experimental) |
| Set up from Windows, macOS, or Linux | [iloader](https://github.com/nab138/iloader), [Impactor](https://github.com/claration/impactor), [Sideloader](https://github.com/Dadoum/Sideloader), [Splice](https://github.com/franklintra/splice) |
| Sign apps on my iPhone with my own certificate | [Feather](https://github.com/claration/feather), [Ksign](https://github.com/Nyasami/Ksign) |
| Run several guest apps inside one signed host | [LiveContainer](https://github.com/LiveContainer/LiveContainer) |
| Install apps without 7-day free-account expiration on **supported** iOS versions | [TrollStore](https://github.com/opa334/TrollStore) |
| Enable JIT in compatible apps | [StikDebug](https://github.com/StikDebug/StikDebug), [SideJITServer](https://github.com/nythepegasus/SideJITServer) |
| Manage or generate device pairing records | [iloader](https://github.com/nab138/iloader), [idevice_pair](https://github.com/jkcoxson/idevice_pair) |

**Read [COMPATIBILITY.md](COMPATIBILITY.md)** before choosing a method. A tool's existence does not mean it works on every iOS version, device, region, or signing method.

## Projects

Short descriptions deliberately keep this page readable. Technical prerequisites, refresh behavior, and compatibility caveats belong in [COMPATIBILITY.md](COMPATIBILITY.md) or the upstream documentation.

### App installers and managers

- **[AltStore Classic](https://github.com/altstoreio/AltStore)** — Open-source app manager that signs IPAs through an Apple Account, with Remote AltServer support since 2.3. [Website](https://altstore.io/). The [2.3.1 release notes](https://github.com/altstoreio/FAQ/blob/main/release-notes/altstore.md) document October 2026 fixes for `-80045`, 2FA and background refresh.
- **[AltLoad](https://github.com/mirazbakis/AltLoad)** — Experimental on-device installer for AltStore, SideStore and LiveContainer. Its author documents iOS 27+ self-pairing; iOS 18–26 requires a pairing file from a computer. Avoid relying on third-party shared certificates/DNS install shortcuts.
- **[Feather](https://github.com/claration/feather)** — Open-source, on-device IPA signing, installation, and source management using developer certificates.
- **[Ksign](https://github.com/Nyasami/Ksign)** — Open-source on-device IPA signer and installer.
- **[LiveContainer](https://github.com/LiveContainer/LiveContainer)** — Runs guest iOS apps inside one signed container. Its [official installation guide](https://livecontainer.github.io/docs/installation) explicitly **does not support Sideloadly or most online signers** for installing LiveContainer; setup and guest compatibility vary.
- **[MultiStore](https://github.com/lungustefan/MultiStore)** — Community SideStore fork that associates apps with multiple Apple Accounts and refreshes them per account; each account still has Apple's limits.
- **[NexStore](https://github.com/NexSideloading/NexStore)** — Open-source, certificate-based on-device app signer and AltStore-source-compatible manager.
- **[RyukSign](https://github.com/faroukbmiled/RyukSign)** — Feather-derived signer with on-device tweak management, local file transfer, and app-source support.
- **[Scarlet](https://usescarlet.com/)** — Proprietary on-device app installer and source manager with direct-install, certificate-based and computer-assisted methods; shared certificates can be revoked. [Developer's GitHub page](https://github.com/DebianArch64/Scarlet).
- **[SideInstaller](https://github.com/FrizzleM/SideInstaller)** — On-device SideStore/LiveContainer setup, including a no-PC path on supported iOS 27+ devices; earlier supported versions may still require a pairing file. **Use only [the author's official download site](https://sideinstaller.net/).**
- **[SideStore](https://github.com/SideStore/SideStore)** — AltStore-derived sideloading manager that installs and refreshes apps on-device after setup. **Avoid 0.6.4 and earlier for current sign-in:** [0.6.4 release notes](https://github.com/SideStore/SideStore/releases/tag/0.6.4) explicitly warn authentication is broken; later alpha/nightly builds may still have issues.
- **[TrollStore](https://github.com/opa334/TrollStore)** — Installs IPAs persistently via a CoreTrust vulnerability on **specific older firmware versions only**.

### Emerging on-device signers

These smaller or newer projects offer interesting functionality, but **activity and a public repository do not demonstrate security, installation reliability, or successful auto-updates**. Prefer original releases and review how certificates and manifests are handled.

- **[BatSign](https://github.com/8yy/BatSign)** — Feather-derived IPA signer claiming background update checks and automated installation; independently verify background operation and iOS prompts.
- **[EnSign](https://github.com/cc158999/EnSign)** — On-device signing manager with source support, tweak injection, and update features; consult its Chinese-language documentation.
- **[ForgeSign](https://github.com/Mesutcydev/ForgeSign-iOS)** — On-device IPA re-signer with certificate management and loopback OTA installation.
- **[SwiftIPA](https://github.com/xsxs18-dev/SwiftIPA)** — Swift on-device signer with IPA inspection, tweak injection, source support, and an optional public manifest relay; check its network/privacy model.
- **[Wax](https://github.com/dylldev/wax-signer)** — Small open-source on-device IPA signing and installation project; early-stage, compatibility not independently verified.

### Hosted signing front ends

**Sensitive trust boundary:** these websites send your IPA and/or **private signing materials** to a remote signing service. A public repository for the website is **not proof that its signing backend is trustworthy**. Prefer local signing where practical, and **never upload your primary development certificate or Apple Account credentials to an untrusted operator**.

- **[Feather Installer](https://github.com/yodaluca23/Feather-Installer)** — Web front end that fetches Feather releases and uses the **third-party ipasign.cc API** to sign/install them; its documentation explicitly says the `.p12`, mobile provisioning profile, and password are transmitted to the service.
- **[Purple Installer](https://github.com/username252510/Purple-Installer)** — Browser-based installer for Feather, Ksign and SideInstaller; sends signing credentials to the **separate Daisuke Signer API**, not just to the front-end website.

### Desktop installers and setup

- **[althea](https://github.com/vyvir/althea)** — Linux GUI for AltServer-Linux with x86_64/ARM support; upstream calls it early-stage.
- **[iloader](https://github.com/nab138/iloader)** — Cross-platform graphical installer for SideStore and IPAs, with pairing-file, certificate, and App ID management.
- **[Impactor](https://github.com/claration/impactor)** — Cross-platform iOS/iPadOS/tvOS sideloading application (formerly PlumeImpactor).
- **[ipaverse](https://github.com/bahattinkoc/ipaverse)** — Apple Silicon macOS app for IPA acquisition, inspection, re-signing, and device installation; downloaded FairPlay-encrypted packages are not automatically re-signable.
- **[iPASide](https://github.com/pwnapplehat/iPASide)** — Open-source Windows-focused IPA installer using an Apple Account.
- **[iOS App Signer](https://github.com/DanTheMan827/ios-app-signer)** — macOS utility for re-signing apps and producing installable IPA files.
- **[IPASIGN](https://github.com/CyberTKR/IpaSigner)** — Qt 6 macOS GUI/CLI for local IPA re-signing with zsign and optional App Store Connect provisioning; early-stage project.
- **[ModStaller](https://github.com/Crafttino21/ModStaller)** — Early-stage Linux/Windows IPA installer with Apple Account signing, Wi-Fi renewal and JIT; upstream claims iOS 27 and tvOS support, but Android-host installation is **planned, not available**.
- **[ios-deploy](https://github.com/ios-control/ios-deploy)** — macOS command-line installation and debugging of apps on physical iOS devices; older development workflow, check recent device support.
- **[Sideloadly](https://sideloadly.io/)** — Windows/macOS sideloading utility with Wi-Fi installation and optional automatic refresh. Proprietary; official website.
- **[Sideloader](https://github.com/Dadoum/Sideloader)** — Open-source cross-platform IPA installation alternative, including Linux.
- **[Splice](https://github.com/franklintra/splice)** — Sideloader fork adding cross-platform, multi-account refresh scheduling and installation management; community-maintained, check supported versions.

### Refresh, AltServer, and self-hosting

- **[AltDaemonModern](https://github.com/emp0ry/AltDaemonModern)** — Rootless-jailbreak-specific AltStore/AltDaemon adaptation for on-device signing; **not** a no-jailbreak alternative.
- **[AltKeeper](https://github.com/BartolomeoRusso9/altkeeper)** — **Experimental** self-hosted AltServer-compatible service for iOS 17+, with Docker, a web UI, and profile-renewal commands. Can serve AltStore Classic over home Wi-Fi; unattended renewal requires Apple credentials stored on the server. Read the upstream test-status and security notes.
- **[AltServer-Linux](https://github.com/NyaMisty/AltServer-Linux)** — Linux port of the AltServer protocol/CLI; review current compatibility and maintenance before deployment.
- **[anisette-v3-server](https://github.com/Dadoum/anisette-v3-server)** — Self-hosted Anisette v1/v3 identity service compatible with SideStore-style signing and AltServer-Linux; Apple authentication changes can break compatibility.
- **[SideStore Anisette server list](https://github.com/SideStore/anisette-servers)** — Official recommended Anisette endpoints and contribution criteria, with machine-readable server metadata; server inclusion does not establish credential trust.
- **[omnisette-server](https://github.com/SideStore/omnisette-server)** — SideStore-maintained HTTP wrapper around Omnisette supporting Anisette v1/v3 protocols.
- **[SideStore Auto Refresh](https://github.com/NRG-Wardog/sidestore-auto-refresh)** — Community project combining LiveContainer and SideStore with an automatic-refresh workflow; check upstream prerequisites.
- **[Sideloop](https://github.com/filippofinke/sideloop)** — Self-hosted Linux/macOS service to re-sign and reinstall IPAs over local Wi-Fi before free provisioning expires; host must remain available and the iPhone unlocked for refresh.
- **[SignTools](https://github.com/SignTools/SignTools)** — Self-hosted web service for signing and installing apps using a macOS signing builder.
- **[Torch](https://github.com/trollzem/torch)** — Experimental macOS menu-bar app for free-account signing and 6-day re-installation of iPhone, iPad and Apple TV IPAs; host must remain available for refresh.
- **[IPA Signer (self-hosted)](https://github.com/aoyn1xw/ipa-signer)** — Node.js/Docker web interface and API for re-signing IPAs with zsign and serving OTA links; **self-host it privately**, as uploaded certificates and app packages reach the server.

**Related:** AltStore Classic 2.3 introduced [Remote AltServer support](https://github.com/altstoreio/AltStore/releases); it is no longer accurate to describe every AltStore setup as requiring a continuously running desktop AltServer.

### Signing and IPA tooling

- **[altsign-cli](https://github.com/xhzq233/altsign-cli)** — macOS CLI for provisioning and re-signing an IPA or .app through a free Apple Account, with managed certificates and 2FA.
- **[IPAID](https://github.com/shplash/IPAID)** — On-device editor for IPA bundle identifiers and app metadata (not a standalone signing service).
- **[ipatool](https://github.com/majd/ipatool)** — CLI to find and download App Store app packages for authorized use; downloading an IPA does not give you redistribution rights.
- **[ldid (Procursus)](https://github.com/ProcursusTeam/ldid)** — Mach-O signing/entitlements utility used in the iOS development and jailbreak ecosystem.
- **[node-applesign](https://github.com/nowsecure/node-applesign)** — Node.js CLI/module for re-signing IPA archives with appropriate signing identities and provisioning assets.
- **[zsign](https://github.com/zhlynn/zsign)** — Cross-platform IPA signing tool for developer workflows.
- **[cyan / pyzule-rw](https://github.com/asdfzxcvbn/pyzule-rw)** — IPA preparation CLI for authorized apps: edits metadata, injects tweaks/frameworks, and prepares output for signing; **not a standalone trusted-certificate signer**.

### Signing and authentication libraries

These are **developer libraries**, not standalone IPA installers. Apple authentication protocols can change without notice; successful signing also requires the correct developer identity and provisioning profile.

- **[AltSign](https://github.com/rileytestut/AltSign)** — AltStore developer's iOS framework for Apple developer accounts and app re-signing.
- **[AnisetteKit](https://github.com/mahee96/AnisetteKit)** — On-device Swift Anisette/ADI emulation library; upstream claims iOS, macOS, tvOS and visionOS support. Apple server compatibility can change.
- **[CodeSignKit](https://github.com/mahee96/CodeSignKit)** — Swift Mach-O/app-bundle signer handling nested frameworks, entitlements and CMS signatures; review its stated AGPL obligations.
- **[GSACryptoKit](https://github.com/mahee96/GSACryptoKit)** — Swift SRP-6a and cryptographic helpers for Apple's GrandSlam Authentication workflow.
- **[SideSign](https://github.com/SideStore/SideSign)** — SideStore-team Swift library for IPA re-signing, developer certificates, provisioning profiles and Apple Developer APIs.

### IPA inspection and authorized research

These help inspect or extract app packages **you own or are authorized to research**. They do not grant permission to bypass DRM or redistribute applications.

- **[frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump)** — Extracts decrypted IPA packages from a jailbroken device for authorized analysis; not a general sideloading installer.
- **[ipa-extract-info](https://github.com/nowsecure/ipa-extract-info)** — Lightweight Node.js/browser library to read `Info.plist` from IPA archives.


### TrollStore ecosystem

- **[TrollApps](https://github.com/TheResonanceTeam/TrollApps)** — Alternative app browser/catalog for TrollStore installations.
- **[TrollFools](https://github.com/Lessica/TrollFools)** — In-place tweak injection for apps on supported TrollStore-based setups.
- **[TrollInstallerX](https://github.com/alfiecg24/TrollInstallerX)** — TrollStore installer for documented iOS 14–16 firmware ranges.
- **[TrollRestore](https://github.com/JJTech0130/TrollRestore)** — Installation route for TrollStore on iOS 17.0.

See the **[main TrollStore project](https://github.com/opa334/TrollStore)** for firmware compatibility and installation guidance.

**Important:** TrollStore installation methods are **firmware-specific**. They do not turn newer iOS versions into generally supported targets.

### JIT and local networking

- **[StikDebug](https://github.com/StikDebug/StikDebug)** — On-device debugger and JIT enabler; supported apps and iOS builds are version-dependent.
- **[StikJIT framework](https://github.com/StikDebug/StikJIT)** — XCFramework for developers integrating on-device JIT workflows; a library, **not** a replacement for the StikDebug end-user app.
- **[SideJITServer](https://github.com/nythepegasus/SideJITServer)** — Desktop-assisted JIT activation for compatible iOS devices.
- **[LocalDevVPN](https://github.com/jkcoxson/LocalDevVPN)** — Loopback networking used by SideStore-related development tools.
- **[minimuxer](https://github.com/jkcoxson/minimuxer)** — On-device lockdown/usbmux-style connectivity library.
- **[em_proxy](https://github.com/jkcoxson/em_proxy)** — Supporting proxy component used by SideStore-style loopback workflows.

JIT capability is **not** implied by successful IPA installation; check the app, device, iOS release, and particular JIT method.

### Device pairing and developer infrastructure

- **[go-ios](https://github.com/danielpaulus/go-ios)** — Cross-platform Go CLI/library for pairing, deploying apps and testing/debugging devices; complements, rather than replaces, an Apple signing identity.
- **[idevice](https://github.com/jkcoxson/idevice)** — Rust libraries for interacting with iOS services.
- **[idevice_pair](https://github.com/jkcoxson/idevice_pair)** — Desktop utility to generate/export pairing records for newer iOS connectivity workflows.
- **[ideviceinstaller](https://github.com/libimobiledevice/ideviceinstaller)** — Command-line management of installed iOS apps.
- **[isideload](https://github.com/nab138/isideload)** — Rust library for sideloading apps, used by iloader.
- **[libplist](https://github.com/libimobiledevice/libplist)** — Parses and writes Apple binary/XML property lists used in IPA metadata and device tooling.
- **[libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)** — Cross-platform iOS device communication protocol library.
- **[libusbmuxd](https://github.com/libimobiledevice/libusbmuxd)** — Client-side USB multiplexing transport used by desktop device-installation utilities.
- **[pymobiledevice3](https://github.com/doronz88/pymobiledevice3)** — Python CLI/library for device pairing, app/profile management, and developer-device services.
- **[usbmuxd](https://github.com/libimobiledevice/usbmuxd)** — Daemon that multiplexes USB connections between host tools and iOS devices.
- **[xtool](https://github.com/xtool-org/xtool)** — Cross-platform SwiftPM/Xcode-alternative developer CLI for building, signing and deploying apps from Linux, Windows/WSL and macOS; not a general IPA source manager.

### App sources and discovery

These are **source catalogs and developer tools**, not assurances that all third-party IPAs are safe or redistributable.

- **[AltDirect](https://github.com/StikDebug/altdirect)** — Redirects AltStore-compatible source URLs to compatible installers.
- **[AltGallery](https://github.com/bebound/AltGallery)** — Discovers AltStore sources and apps hosted by projects on GitHub.
- **[iOS Hub](https://github.com/CaseyCZ/iOS-Hub)** — Community-maintained live source directory with availability checks, source builder, installer guidance and troubleshooting; **online means reachable, not safe**.
- **[appdb](https://appdb.to/)** — Proprietary app-discovery and installation platform; availability and certificate/signing requirements vary by workflow.
- **[AltSource Viewer](https://github.com/therealFoxster/altsource-viewer)** — Viewer for AltStore-format sources.
- **[awesome-altstore](https://github.com/victordedomenico/awesome-altstore)** — Separate curated collection focused on AltStore JSON sources.
- **[SideStore Community Source](https://github.com/SideStore/Community-Source)** — Official SideStore community/trusted source submission project.
- **[SideStore Official Source](https://github.com/SideStore/apps.json)** — Official AltSource feed for SideStore and related project releases; typically preconfigured in SideStore.
- **[SideStoreAndAltStore-Sources](https://github.com/luh-99/SideStoreAndAltStore-Sources)** — Community collection of source URLs for AltStore and SideStore.
- **[Sideload-Sources](https://github.com/KB01111/Sideload-Sources)** — Community source pointing to upstream GitHub Release assets; verify individual apps before installing.
- **[ShrubLibrary](https://github.com/ShrubHub-iOS/ShrubLibrary)** — Web directory of iOS apps and AltStore-compatible repositories, with search and source import; **repository documents the website, not its source code**, and third-party IPA listings aren't vetted.

### Self-hosted distribution and app sources

- **[App Distribution Server](https://github.com/significa/app-distribution-server)** — Docker service for distributing **already signed** iOS IPA/Android APK builds through an installation page and QR code; no Apple Account signing or provisioning. Change its documented default upload token before deployment.

- **[GithubStore](https://github.com/yazdipour/GithubStore)** — Docker-hosted AltStore/SideStore/LiveContainer feed generated from selected GitHub releases; optional configuration web UI has **no authentication** and should stay private.
- **[TeleStore](https://github.com/yazdipour/TeleStore)** — Self-hosted AltStore-compatible feed from Telegram channels; requires your Telegram API credentials/session and may expose unauthorized third-party IPAs. Use only channels and apps you have rights to distribute.


### Projects in development

- **[StikStore](https://stikstore.app/)** — Announced on-device app manager with planned Apple Account/certificate signing and JIT. **Not yet a generally released solution** at the time of review; distinguish roadmap features from working functionality.

### Apple TV and legacy devices

- **[atvloadly](https://github.com/bitxeno/atvloadly)** — Apple TV IPA sideloading and self-hosted workflows.
- **[atv-sideload](https://github.com/Lauch2/atv-sideload)** — Experimental Linux scripts to package tvOS apps and install them via a separately supplied `plumesign` binary. Upstream pairing scripts are incomplete; not a turnkey installer.
- **[Legacy iOS Kit](https://github.com/LukeZGD/Legacy-iOS-Kit)** — Toolkit for older iOS devices with a [Linux sideloading guide](https://github.com/LukeZGD/Legacy-iOS-Kit/wiki/Sideloading-on-Linux). Best treated separately from modern signing methods.

## Region-specific marketplaces

**Apple-authorized alternative distribution is different from arbitrary IPA sideloading.** Eligibility depends on both region and OS version.

- **[AltStore PAL](https://altstore.io/)** — Apple's alternative-distribution framework-based marketplace for supported regions; distinct from AltStore Classic.
- **[Apple: About alternative app distribution](https://support.apple.com/en-ie/118110)** — Official user-facing regional and device eligibility rules.
- **[Apple: Alternative distribution by region](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions)** — Official developer requirements.

## Documentation

- [AltStore official website and setup](https://altstore.io/)
- [AltStore developer documentation](https://developer.altstore.io/)
- [SideStore documentation](https://docs.sidestore.io/)
- [AltStore Classic release notes](https://github.com/altstoreio/FAQ/blob/main/release-notes/altstore.md) — Version-specific sign-in fixes and remote refresh updates.
- [LiveContainer official installation guide](https://livecontainer.github.io/docs/installation) — Supported installers and the differences between standalone and combined SideStore builds.
- [Sideloadly official FAQ](https://sideloadly.io/faq.html) — Device setup, Windows USB drivers, Wi-Fi refresh, signing limits and Apple TV caveats.
- [SideStore JIT guide](https://docs.sidestore.io/docs/advanced/jit)
- [iOS Hub sideloading comparison](https://caseycz.github.io/iOS-Hub/guide.html) — Community-maintained overview; double-check claims against upstream.
- [Apple Developer: Code signing](https://developer.apple.com/support/code-signing/)
- [Compatibility and caveats in this repository](COMPATIBILITY.md)
- [SideStore: reported October 2026 Apple ID login errors](https://github.com/SideStore/SideStore/issues/1647) — Follow maintainer updates rather than copying outdated Anisette identity strings from old guides.
- [SideStore: community authentication troubleshooting](https://github.com/orgs/SideStore/discussions/1666) — Discussion of temporary `-80045` / HTTP 503 / 2FA problems; solutions vary by build.

## Research notes and scope

The [research notes](RESEARCH_NOTES.md) explain which entries from [awesome-iOS-security-tools](https://github.com/0xdad0/awesome-iOS-security-tools) were relevant, which broader security tools were intentionally not copied, and the additional sources reviewed in October 2026. A newer commit, a GitHub star count, and inclusion in this list **are not independent functionality or security verification**.

## Communities and support

These are independent discussion and support venues, **not verified download sources**. For installation binaries and credentials, follow the original project's documentation rather than unsolicited messages, mirrors, or certificates shared in a chat.

- **[r/AltStore](https://www.reddit.com/r/AltStore/)** — AltStore Classic/PAL, AltServer, installation and provisioning troubleshooting; compare community advice against [official AltStore documentation](https://faq.altstore.io/).
- **[r/jailbreak](https://www.reddit.com/r/jailbreak/)** — Adjacent jailbreak/firmware and TrollStore discussions; **not** a substitute for normal sideloading support and not every jailbreak applies to every OS version.
- **[r/LegacyJailbreak](https://www.reddit.com/r/LegacyJailbreak/)** — Older iPhones/iPads, firmware-specific sideloading limitations and legacy installation tools.
- **[r/Sideloadly](https://www.reddit.com/r/Sideloadly/)** — Sideloadly-specific setup, daemon, Wi-Fi and signing issues; linked by the project's [official FAQ](https://sideloadly.io/faq.html).
- **[r/SideStore](https://www.reddit.com/r/SideStore/)** — Community reports on SideStore login, pairing and background renewal; check claims against maintainer releases.
- **[r/Trollstore](https://www.reddit.com/r/Trollstore/)** — TrollStore and jailbreak-dependent TrollStore Lite discussions; not all methods support the same firmware.
- **[r/sideloaded](https://www.reddit.com/r/sideloaded/)** — Large subreddit dedicated to non-jailbreak sideloading tools, setup, troubleshooting and release discussions. [Community Discord](https://discord.gg/pUHBuxYzSG) is advertised by the subreddit; its invite may change.
- **[SideStore Discord](https://discord.gg/sidestore)** — Official community support linked from the [verified SideStore organization](https://github.com/SideStore). Also see [SideStore Discussions](https://github.com/orgs/SideStore/discussions) for feature reports and reproducible issues.
- **[Apple Developer Forums: Code Signing](https://developer.apple.com/forums/topics/code-signing-topic/code-signing-topic-general)** — Primary-source discussion for signing identities, entitlements and provisioning-profile problems; not support for unauthorized signing services.
- **[iOS Guide](https://ios.cfw.guide/installing-trollstore/)** — Firmware-specific TrollStore installation instructions and links to the wider iOS jailbreak community; firmware-specific guidance is essential.
- **[GitHub sideloading topic](https://github.com/topics/sideloading)** and **[SideStore topic](https://github.com/topics/sidestore)** — Discover upstream repositories; tags and recent commits do not independently establish security or working compatibility.

## Safety and limitations

- **Apple Account:** free development signing usually means **7-day provisioning**, plus App ID/active-app limits. Auto-refresh reduces manual work; it does not remove Apple's limits. Paid certificates have different rules and can still be revoked.
- **Credentials:** use official tools and inspect how they handle passwords, 2FA, pairing records, and .p12 certificates. A pairing record and a signing identity are sensitive secrets. **A website that forwards your .p12 and its password to a third-party API crosses a major trust boundary.**
- **AltKeeper:** its unattended-renewal mode documents a saved Apple Account password in clear text with restricted file permissions. Do not expose its storage, logs, web UI, or AltServer endpoint to the public internet without carefully reviewing the threat model.
- **Certificates:** never upload a private .p12, password, or provisioning file to a web signer without independently assessing the operator. Publicly shared enterprise certificates, DNS blocking tricks, and third-party pre-signed IPAs can be unreliable or unsafe. They are not presented as equivalent to your own signing identity.
- **Compatibility:** iOS 17, 18, 26, and 27 have meaningfully different pairing, JIT, and signing paths. Do not generalize a result across firmware versions. October 2026 Apple-authentication changes have also broken some Anisette/client identity combinations; see [the current troubleshooting notes](COMPATIBILITY.md#october-2026-apple-id-anisette-disruptions).
- **Legality and trust:** only install software you are authorized to use, and prefer releases and source code from the original maintainer. A source directory's `online` status only establishes that its feed could be reached, not that the distributed IPA is authentic, legal or safe.

## License

This list's original compilation and descriptions are dedicated to the public domain under [CC0 1.0](LICENSE). Linked projects retain **their own** licenses and copyrights.

## Contributing

Add a genuinely relevant project, correct an outdated compatibility note, or report a broken link via an [issue](https://github.com/lgg/awesome-ios-sideloading/issues) or [pull request](https://github.com/lgg/awesome-ios-sideloading/pulls). See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria, evidence requirements, and the preferred entry format.

This list is maintained independently and is **not affiliated with Apple, AltStore, SideStore, or other listed projects**.
