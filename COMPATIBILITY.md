# Compatibility and setup notes

> An intentionally compact companion to [README.md](README.md). The main list stays easy to scan; this document records setup differences, signing constraints, and known limitations.

**Last reviewed:** 2026-10-25. **Legend:** `Yes` = feature documented by the maintainer; `Setup` = computer needed for initial pairing/bootstrap; `Varies` = depends on the particular installation method, certificate, or firmware; `—` = not applicable. **Not a hands-on test certification.**

## Choose an installation workflow

| Project | Primary use | Computer / host | Signing or refresh model | Important caveat |
| --- | --- | --- | --- | --- |
| [AltStore Classic](https://github.com/altstoreio/AltStore) | Install and update IPA files | Windows/macOS AltServer, **or configured Remote AltServer** | Personal Apple Account; normal profile renewal | AltStore Classic 2.3 added Remote AltServer; remote functionality still needs a suitable server/backend |
| [SideStore](https://github.com/SideStore/SideStore) | Install/refresh on device | Setup / pairing path varies | Personal Apple Account; on-device renewal with local VPN transport | Initial setup and VPN/pairing requirements vary by OS |
| [Sideloadly](https://sideloadly.io/) | Direct desktop installation | Windows/macOS | Free/paid account; optional desktop auto-refresh | Needs running desktop for automated refresh; JIT is version-restricted |
| [iloader](https://github.com/nab138/iloader) | SideStore and IPA setup | Windows/macOS/Linux | Installer and pairing manager | A setup tool; not an independent background refresh service |
| [Impactor](https://github.com/claration/impactor) | Cross-platform sideloading | Desktop (see upstream builds) | Depends on signing mode | Check available releases and platform instructions |
| [Feather](https://github.com/claration/feather) | On-device IPA sign and install | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate expiry/revocation still applies |
| [Ksign](https://github.com/Nyasami/Ksign) | On-device IPA signing | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate provenance matters |
| [LiveContainer](https://github.com/LiveContainer/LiveContainer) | Run guest apps inside a host | Host app must first be installed | Host's signing/refresh applies | Not every IPA or entitlement works inside a container |
| [TrollStore](https://github.com/opa334/TrollStore) | Persistent installation | Depends on firmware-specific bootstrap | Exploit-based; not 7-day personal provisioning | Official supported firmware ranges only |
| [SideInstaller](https://github.com/FrizzleM/SideInstaller) | On-device SideStore bootstrap | On iOS 27+: no PC path; earlier: pairing-file prerequisites | SideStore/free-account workflow after install | Author documents iOS 17.4+, with different pairing requirements |
| [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) | Self-hosted AltServer and renewal | Always-on home machine; USB pairing once | AltStore protocol plus optional unattended profile renewal | **Experimental**; unattended mode stores account password on host |
| [SideStore Auto Refresh](https://github.com/NRG-Wardog/sidestore-auto-refresh) | Community automatic-refresh workflow | Device/setup-dependent | Free Apple Account and SideStore-based process | Check upstream installation method and restrictions |
| [SignTools](https://github.com/SignTools/SignTools) | Self-hosted signing web UI | Service host + macOS builder | Signing certificates and profiles | Builder/signing infrastructure needed |
| [AltServer-Linux](https://github.com/NyaMisty/AltServer-Linux) | AltServer-compatible Linux daemon | Linux host | Apple-account-based signing | Older project; check recent issues/releases first |
| [atvloadly](https://github.com/bitxeno/atvloadly) | Apple TV sideloading | Linux/OpenWrt or other supported host | Device and account dependent | tvOS support is separate from iOS |

## Important platform distinctions

### AltStore Classic versus AltStore PAL

- **Classic:** IPA sideloading with an Apple Account, typically subject to development-signing limits. AltServer can be local or, with supported new versions and correct setup, remote.
- **PAL:** A region-eligible, Apple-notarized alternative marketplace. It is **not** a replacement for unrestricted IPA sideloading and does not use Classic's usual 7-day personal-development signing model.
- Refer to the [AltStore releases](https://github.com/altstoreio/AltStore/releases) and [Apple's official regional rules](https://support.apple.com/en-ie/118110).

### Free Apple Account

Free personal-development provisioning normally expires after **7 days**, and the number of active sideloaded apps and registered App IDs is limited. AltStore documents a common limit of **3 active apps** and **10 App IDs**, with exceptions and changing behavior possible. Apps installed through other certificates, TrollStore, or authorized alternative marketplaces follow **different rules**.

### TrollStore

- Support is tied to vulnerable iOS/iPadOS firmware, **not just hardware generation**.
- The original TrollStore documents iOS **14.0 beta 2–16.6.1**, **16.7 RC**, and **17.0** on compatible devices; check [official install documentation](https://github.com/opa334/TrollStore) and the exact build.
- [TrollInstallerX](https://github.com/alfiecg24/TrollInstallerX) and [TrollRestore](https://github.com/JJTech0130/TrollRestore) cover particular installation paths and do not expand the exploit's supported OS range.

### JIT: do not promise blanket compatibility

A JIT tool successfully connecting to a phone does not prove that an emulator or other target app can run JIT. App support changes between iOS revisions. The [SideStore JIT guide](https://docs.sidestore.io/docs/advanced/jit) maintains current caveats. [StikDebug](https://github.com/StikDebug/StikDebug) and [SideJITServer](https://github.com/nythepegasus/SideJITServer) use different routes; always follow the chosen tool's latest prerequisites.

### Pairing files and local networking

Newer iOS versions can require **remote pairing** records rather than older lockdown pairing files for some loopback workflows. [iloader](https://github.com/nab138/iloader), [idevice_pair](https://github.com/jkcoxson/idevice_pair), and [SideInstaller](https://github.com/FrizzleM/SideInstaller) provide documentation and/or workflows for this. **Never upload pairing records to a public issue.**

## AltKeeper: documented behavior and open tests

[AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) deserves particular care because its functionality is broader than a simple IPA installer:

- **AltServer mode:** responds to AltStore Classic's installation and refresh requests on the local network, without requiring the Apple password on the AltKeeper host for this mode.
- **Standalone `renew` / scheduled mode:** renews provisioning profiles without opening AltStore, but requires Apple Account credentials stored on the host. The upstream README says the password is stored **in clear text** in a permission-restricted `account.json`.
- **Upstream tests:** documented on macOS and Debian x86-64 Docker with real devices; Windows 10 native build, tests and interactive login were verified, while some end-to-end Windows and long-duration scenarios remained unverified at the time of review.
- **Status:** experimental; upstream specifically notes that expiration-day behavior and long-running operation have not yet been fully tested. No JIT support.

For safe deployment, keep it **LAN-only**, protect its pairing file, account state, and web UI, and follow upstream updates before treating it as a set-and-forget renewal solution.

## Maintenance and evidence

When changing a compatibility claim, include the **device**, **iOS/iPadOS version**, **tool version**, **signing type**, **date**, and a link to upstream documentation, changelog, or reproducible test notes. Add a statement like _not independently verified_ if the change only reflects a maintainer's claim.

Avoid hardcoding latest iOS numbers as permanent project features; devices, regions, certificates, and OS releases change faster than static lists.

Back to [Awesome iOS Sideloading](README.md).
