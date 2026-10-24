# Awesome iOS Sideloading

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated list of tools and resources for sideloading apps on iOS, iPadOS, and tvOS: installers, signing utilities, self-hosted servers, JIT, pairing tools, and app sources.

**[Find a tool](#start-here)** · **[Projects](#projects)** · **[Compatibility](COMPATIBILITY.md)** · **[Contribute](CONTRIBUTING.md)**

This list focuses on **the sideloading ecosystem itself**, not collections of modified or pirated IPA files. Links prefer original developers and primary documentation. Inclusion is **not an endorsement or a security audit**. Project availability, signing restrictions, iOS support, and maintenance can change.

_Last catalog review: 2026-10-25. Individual entries are not all tested on physical devices._

## Contents

- [Start here](#start-here)
- [Projects](#projects)
  - [App installers and managers](#app-installers-and-managers)
  - [Desktop installers and setup](#desktop-installers-and-setup)
  - [Refresh, AltServer, and self-hosting](#refresh-altserver-and-self-hosting)
  - [Signing and IPA tooling](#signing-and-ipa-tooling)
  - [TrollStore ecosystem](#trollstore-ecosystem)
  - [JIT and local networking](#jit-and-local-networking)
  - [Device pairing and developer infrastructure](#device-pairing-and-developer-infrastructure)
  - [App sources and discovery](#app-sources-and-discovery)
  - [Apple TV and legacy devices](#apple-tv-and-legacy-devices)
- [Region-specific marketplaces](#region-specific-marketplaces)
- [Documentation](#documentation)
- [Safety and limitations](#safety-and-limitations)
- [Contributing](#contributing)

## Start here

| I want to… | Good starting points |
| --- | --- |
| Install IPAs using a free Apple Account | [AltStore Classic](https://github.com/altstoreio/AltStore), [SideStore](https://github.com/SideStore/SideStore), [Sideloadly](https://sideloadly.io/) |
| Refresh apps without relying on a desktop session | [SideStore](https://github.com/SideStore/SideStore), [AltStore Classic + Remote AltServer](https://github.com/altstoreio/AltStore/releases), [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) (experimental) |
| Set up from Windows, macOS, or Linux | [iloader](https://github.com/nab138/iloader), [Impactor](https://github.com/claration/impactor), [Sideloader](https://github.com/Dadoum/Sideloader) |
| Sign apps on my iPhone with my own certificate | [Feather](https://github.com/claration/feather), [Ksign](https://github.com/Nyasami/Ksign) |
| Run several guest apps inside one signed host | [LiveContainer](https://github.com/LiveContainer/LiveContainer) |
| Install apps without 7-day free-account expiration on **supported** iOS versions | [TrollStore](https://github.com/opa334/TrollStore) |
| Enable JIT in compatible apps | [StikDebug](https://github.com/StikDebug/StikDebug), [SideJITServer](https://github.com/nythepegasus/SideJITServer) |
| Manage or generate device pairing records | [iloader](https://github.com/nab138/iloader), [idevice_pair](https://github.com/jkcoxson/idevice_pair) |

**Read [COMPATIBILITY.md](COMPATIBILITY.md)** before choosing a method. A tool's existence does not mean it works on every iOS version, device, region, or signing method.

## Projects

Short descriptions deliberately keep this page readable. Technical prerequisites, refresh behavior, and compatibility caveats belong in [COMPATIBILITY.md](COMPATIBILITY.md) or the upstream documentation.

### App installers and managers

- **[AltStore Classic](https://github.com/altstoreio/AltStore)** — Open-source app manager that signs IPAs through an Apple Account; recent versions also support remote AltServer setups. [Website](https://altstore.io/).
- **[Feather](https://github.com/claration/feather)** — Open-source, on-device IPA signing, installation, and source management using developer certificates.
- **[Ksign](https://github.com/Nyasami/Ksign)** — Open-source on-device IPA signer and installer.
- **[LiveContainer](https://github.com/LiveContainer/LiveContainer)** — Runs guest iOS apps inside a signed container rather than installing each guest as a separate Home Screen app; some apps and capabilities are incompatible.
- **[SideStore](https://github.com/SideStore/SideStore)** — AltStore-derived sideloading manager designed to install and refresh apps on-device after setup.
- **[TrollStore](https://github.com/opa334/TrollStore)** — Installs IPAs persistently via a CoreTrust vulnerability on **specific older firmware versions only**.

### Desktop installers and setup

- **[iloader](https://github.com/nab138/iloader)** — Cross-platform graphical installer for SideStore and IPAs, with pairing-file, certificate, and App ID management.
- **[Impactor](https://github.com/claration/impactor)** — Cross-platform iOS/iPadOS/tvOS sideloading application (formerly PlumeImpactor).
- **[iPASide](https://github.com/pwnapplehat/iPASide)** — Open-source Windows-focused IPA installer using an Apple Account.
- **[iOS App Signer](https://github.com/DanTheMan827/ios-app-signer)** — macOS utility for re-signing apps and producing installable IPA files.
- **[Sideloadly](https://sideloadly.io/)** — Windows/macOS sideloading utility with Wi-Fi installation and optional automatic refresh. Proprietary; official website.
- **[Sideloader](https://github.com/Dadoum/Sideloader)** — Open-source cross-platform IPA installation alternative, including Linux.
- **[SideInstaller](https://github.com/FrizzleM/SideInstaller)** — On-device SideStore/LiveContainer setup, including a no-PC path on supported iOS 27+ devices; earlier supported versions may still require a pairing file. **Use only [the author's official download site](https://sideinstaller.net/).**

### Refresh, AltServer, and self-hosting

- **[AltKeeper](https://github.com/BartolomeoRusso9/altkeeper)** — **Experimental** self-hosted AltServer-compatible service for iOS 17+, with Docker, a web UI, and profile-renewal commands. Can serve AltStore Classic over home Wi-Fi; unattended renewal requires Apple credentials stored on the server. Read the upstream test-status and security notes.
- **[AltServer-Linux](https://github.com/NyaMisty/AltServer-Linux)** — Linux port of the AltServer protocol/CLI; review current compatibility and maintenance before deployment.
- **[SideStore Auto Refresh](https://github.com/NRG-Wardog/sidestore-auto-refresh)** — Community project combining LiveContainer and SideStore with an automatic-refresh workflow; check upstream prerequisites.
- **[SignTools](https://github.com/SignTools/SignTools)** — Self-hosted web service for signing and installing apps using a macOS signing builder.

**Related:** AltStore Classic 2.3 introduced [Remote AltServer support](https://github.com/altstoreio/AltStore/releases); it is no longer accurate to describe every AltStore setup as requiring a continuously running desktop AltServer.

### Signing and IPA tooling

- **[ipatool](https://github.com/majd/ipatool)** — CLI to find and download App Store app packages for authorized use; downloading an IPA does not give you redistribution rights.
- **[ldid (Procursus)](https://github.com/ProcursusTeam/ldid)** — Mach-O signing/entitlements utility used in the iOS development and jailbreak ecosystem.
- **[zsign](https://github.com/zhlynn/zsign)** — Cross-platform IPA signing tool for developer workflows.
- **[TrollFools](https://github.com/Lessica/TrollFools)** — In-place tweak injection for apps on supported TrollStore-based setups.

### TrollStore ecosystem

- **[TrollInstallerX](https://github.com/alfiecg24/TrollInstallerX)** — TrollStore installer for documented iOS 14–16 firmware ranges.
- **[TrollRestore](https://github.com/JJTech0130/TrollRestore)** — Installation route for TrollStore on iOS 17.0.
- **[TrollApps](https://github.com/TheResonanceTeam/TrollApps)** — Alternative app browser/catalog for TrollStore installations.
- **[TrollStore](https://github.com/opa334/TrollStore)** — Main project, official compatibility range, and installation guidance.

**Important:** TrollStore installation methods are **firmware-specific**. They do not turn newer iOS versions into generally supported targets.

### JIT and local networking

- **[StikDebug](https://github.com/StikDebug/StikDebug)** — On-device debugger and JIT enabler; supported apps and iOS builds are version-dependent.
- **[SideJITServer](https://github.com/nythepegasus/SideJITServer)** — Desktop-assisted JIT activation for compatible iOS devices.
- **[LocalDevVPN](https://github.com/jkcoxson/LocalDevVPN)** — Loopback networking used by SideStore-related development tools.
- **[minimuxer](https://github.com/jkcoxson/minimuxer)** — On-device lockdown/usbmux-style connectivity library.
- **[em_proxy](https://github.com/jkcoxson/em_proxy)** — Supporting proxy component used by SideStore-style loopback workflows.

JIT capability is **not** implied by successful IPA installation; check the app, device, iOS release, and particular JIT method.

### Device pairing and developer infrastructure

- **[idevice](https://github.com/jkcoxson/idevice)** — Rust libraries for interacting with iOS services.
- **[idevice_pair](https://github.com/jkcoxson/idevice_pair)** — Desktop utility to generate/export pairing records for newer iOS connectivity workflows.
- **[ideviceinstaller](https://github.com/libimobiledevice/ideviceinstaller)** — Command-line management of installed iOS apps.
- **[isideload](https://github.com/nab138/isideload)** — Rust library for sideloading apps, used by iloader.
- **[libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)** — Cross-platform iOS device communication protocol library.
- **[pymobiledevice3](https://github.com/doronz88/pymobiledevice3)** — Python CLI/library for device pairing, app/profile management, and developer-device services.

### App sources and discovery

These are **source catalogs and developer tools**, not assurances that all third-party IPAs are safe or redistributable.

- **[AltDirect](https://github.com/StikDebug/altdirect)** — Redirects AltStore-compatible source URLs to compatible installers.
- **[AltGallery](https://github.com/bebound/AltGallery)** — Discovers AltStore sources and apps hosted by projects on GitHub.
- **[AltSource Viewer](https://github.com/therealFoxster/altsource-viewer)** — Viewer for AltStore-format sources.
- **[awesome-altstore](https://github.com/victordedomenico/awesome-altstore)** — Separate curated collection focused on AltStore JSON sources.
- **[SideStore Community Source](https://github.com/SideStore/Community-Source)** — Official SideStore community/trusted source submission project.
- **[SideStoreAndAltStore-Sources](https://github.com/luh-99/SideStoreAndAltStore-Sources)** — Community collection of source URLs for AltStore and SideStore.
- **[Sideload-Sources](https://github.com/KB01111/Sideload-Sources)** — Community source pointing to upstream GitHub Release assets; verify individual apps before installing.

### Apple TV and legacy devices

- **[atvloadly](https://github.com/bitxeno/atvloadly)** — Apple TV IPA sideloading and self-hosted workflows.
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
- [SideStore JIT guide](https://docs.sidestore.io/docs/advanced/jit)
- [iOS Hub sideloading comparison](https://caseycz.github.io/iOS-Hub/guide.html) — Community-maintained overview; double-check claims against upstream.
- [Apple Developer: Code signing](https://developer.apple.com/support/code-signing/)
- [Compatibility and caveats in this repository](COMPATIBILITY.md)

## Safety and limitations

- **Apple Account:** free development signing usually means **7-day provisioning**, plus App ID/active-app limits. Auto-refresh reduces manual work; it does not remove Apple's limits. Paid certificates have different rules and can still be revoked.
- **Credentials:** use official tools and inspect how they handle passwords, 2FA, pairing records, and .p12 certificates. A pairing record and a signing identity are sensitive secrets.
- **AltKeeper:** its unattended-renewal mode documents a saved Apple Account password in clear text with restricted file permissions. Do not expose its storage, logs, web UI, or AltServer endpoint to the public internet without carefully reviewing the threat model.
- **Certificates:** publicly shared enterprise certificates, DNS blocking tricks, and third-party pre-signed IPAs can be unreliable or unsafe. They are not presented as equivalent to your own signing identity.
- **Compatibility:** iOS 17, 18, 26, and 27 have meaningfully different pairing, JIT, and signing paths. Do not generalize a result across firmware versions.
- **Legality and trust:** only install software you are authorized to use, and prefer releases and source code from the original maintainer.

## Contributing

Add a genuinely relevant project, correct an outdated compatibility note, or report a broken link via an [issue](https://github.com/lgg/awesome-ios-sideloading/issues) or [pull request](https://github.com/lgg/awesome-ios-sideloading/pulls). See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria, evidence requirements, and the preferred entry format.

This list is maintained independently and is **not affiliated with Apple, AltStore, SideStore, or other listed projects**.
