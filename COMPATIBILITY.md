# Compatibility and setup notes

> An intentionally compact companion to [README.md](README.md). The main list stays easy to scan; this document records setup differences, signing constraints, and known limitations.

**Last reviewed:** 2026-10-25. **Legend:** `Yes` = feature documented by the maintainer; `Setup` = computer needed for initial pairing/bootstrap; `Varies` = depends on the particular installation method, certificate, or firmware; `—` = not applicable. **Not a hands-on test certification.**

## Choose an installation workflow

| Project | Primary use | Computer / host | Signing or refresh model | Important caveat |
| --- | --- | --- | --- | --- |
| [AltStore Classic](https://github.com/altstoreio/AltStore) | Install and update IPA files | Windows/macOS AltServer, **or configured Remote AltServer** | Personal Apple Account; normal profile renewal | AltStore Classic 2.3 added Remote AltServer; remote functionality still needs a suitable server/backend |
| [SideStore](https://github.com/SideStore/SideStore) | Install/refresh on device | Setup / pairing path varies | Personal Apple Account; on-device renewal with local VPN transport | Initial setup and VPN/pairing requirements vary by OS |
| [Scarlet](https://usescarlet.com/) | On-device IPA installation, app sources, and tweak injection | Depends on installation mode (direct, computer, own certificate) | Shared certificate, personal developer account, or owned signing assets | Proprietary; direct/shared-certificate route can be revoked or unavailable |
| [MultiStore](https://github.com/lungustefan/MultiStore) | Manage SideStore installs across Apple IDs | Initial setup/pairing via iloader or similar | Per-app signing identity, refresh grouped by Apple Account | Community fork; multiple accounts do **not** remove per-account or per-device Apple limits |
| [Sideloadly](https://sideloadly.io/) | Direct desktop installation | Windows/macOS | Free/paid account; optional desktop auto-refresh | Needs running desktop for automated refresh; JIT is version-restricted |
| [IPASIGN](https://github.com/CyberTKR/IpaSigner) | Desktop IPA re-signing and profile setup | macOS + Qt 6/Xcode command-line tools | Locally supplied signing identity, optional App Store Connect API keys | Early-stage; verify handling of privileged developer credentials and artifacts |
| [Feather Installer](https://github.com/yodaluca23/Feather-Installer) | Browser-assisted Feather bootstrap | Browser + **third-party ipasign.cc backend** | Uploaded `.p12`, profile and password | **Sensitive signing materials sent to third-party API**; use only with an appropriately isolated identity |
| [Purple Installer](https://github.com/username252510/Purple-Installer) | Hosted web bootstrap for Feather/Ksign/SideInstaller | Browser + **third-party Daisuke Signer backend** | Uploaded `.p12`, profile and password | Browser local storage does not prevent material being sent to remote signer |
| [iloader](https://github.com/nab138/iloader) | SideStore and IPA setup | Windows/macOS/Linux | Installer and pairing manager | A setup tool; not an independent background refresh service |
| [Impactor](https://github.com/claration/impactor) | Cross-platform sideloading | Desktop (see upstream builds) | Depends on signing mode | Check available releases and platform instructions |
| [althea](https://github.com/vyvir/althea) | GUI for AltServer-Linux | Linux desktop or supported ARM host | AltServer-Linux and Apple Account | Upstream marks project early-stage; do not assume support for every new iOS |
| [Splice](https://github.com/franklintra/splice) | Desktop sideloading and scheduled refresh | Linux, Windows or macOS (consult releases) | Apple Account re-sign/reinstall | Maintained fork of Sideloader; automatic refresh claims not independently tested |
| [ipaverse](https://github.com/bahattinkoc/ipaverse) | App Store downloads, IPA inspection and installation | **Apple Silicon macOS 14.6+** | Personal signing certificate/profile for DRM-free IPA | FairPlay-encrypted App Store downloads are **not directly re-signable** |
| [Feather](https://github.com/claration/feather) | On-device IPA sign and install | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate expiry/revocation still applies |
| [Ksign](https://github.com/Nyasami/Ksign) | On-device IPA signing | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate provenance matters |
| [SwiftIPA](https://github.com/xsxs18-dev/SwiftIPA) | On-device re-sign, IPA edit and OTA installation | iPhone/iPad (iOS 16+ claimed by upstream) | Your .p12 and provisioning profile | Early-stage; author documents optional public relay **for manifest metadata** |
| [BatSign](https://github.com/8yy/BatSign) | On-device signing, background updates | iOS 16+ claimed by upstream | Certificate-based | Automated installs/notifications are upstream claims; test on real devices and firmware |
| [ForgeSign](https://github.com/Mesutcydev/ForgeSign-iOS) | On-device IPA re-signing and OTA install | iOS device | Your .p12 and profile | Check releases and supported firmware |
| [EnSign](https://github.com/cc158999/EnSign) | On-device signing and update workflow | iPhone/iPad | Certificate-based | Check upstream docs and independent security evidence |
| [LiveContainer](https://github.com/LiveContainer/LiveContainer) | Run guest apps inside a host | Host app must first be installed | Host's signing/refresh applies | Not every IPA or entitlement works inside a container |
| [TrollStore](https://github.com/opa334/TrollStore) | Persistent installation | Depends on firmware-specific bootstrap | Exploit-based; not 7-day personal provisioning | Official supported firmware ranges only |
| [SideInstaller](https://github.com/FrizzleM/SideInstaller) | On-device SideStore bootstrap | On iOS 27+: no PC path; earlier: pairing-file prerequisites | SideStore/free-account workflow after install | Author documents iOS 17.4+, with different pairing requirements |
| [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) | Self-hosted AltServer and renewal | Always-on home machine; USB pairing once | AltStore protocol plus optional unattended profile renewal | **Experimental**; unattended mode stores account password on host |
| [Sideloop](https://github.com/filippofinke/sideloop) | Scheduled re-sign/reinstall over Wi-Fi | Linux/macOS Docker server; pairing initially via USB | Free Apple Account with AltServer-Linux | Device must be unlocked, nearby, and on same Wi-Fi during refresh; 2FA and credentials on server |
| [AltDaemonModern](https://github.com/emp0ry/AltDaemonModern) | Jailbroken on-device refresh/signing | Rootless jailbreak and compatible package setup | Apple Account / AltDaemon | Requires jailbreak; **not** equivalent to SideStore on jailed devices |
| [SideStore Auto Refresh](https://github.com/NRG-Wardog/sidestore-auto-refresh) | Community automatic-refresh workflow | Device/setup-dependent | Free Apple Account and SideStore-based process | Check upstream installation method and restrictions |
| [SignTools](https://github.com/SignTools/SignTools) | Self-hosted signing web UI | Service host + macOS builder | Signing certificates and profiles | Builder/signing infrastructure needed |
| [IPA Signer](https://github.com/aoyn1xw/ipa-signer) | Self-hosted web/API signing + OTA download | Linux/macOS + Node.js 22+ or Docker | Provided certificate, profile and IPA uploaded to the server | **Keep behind authentication/private network**; web-signing upload endpoint is sensitive |
| [GithubStore](https://github.com/yazdipour/GithubStore) | Self-hosted AltStore source generated from GitHub Releases | Docker host | Feeds original GitHub IPA release URLs | Optional configuration UI has **no authentication**; scope to trusted upstream repos |
| [TeleStore](https://github.com/yazdipour/TeleStore) | Self-hosted AltStore source from Telegram channels | Docker host + Telegram API/session | Telegram-channel IPA assets | Protect Telegram session; only distribute apps with permission |
| [AltServer-Linux](https://github.com/NyaMisty/AltServer-Linux) | AltServer-compatible Linux daemon | Linux host | Apple-account-based signing | Older project; check recent issues/releases first |
| [atvloadly](https://github.com/bitxeno/atvloadly) | Apple TV sideloading | Linux/OpenWrt or other supported host | Device and account dependent | tvOS support is separate from iOS |

## Signing, metadata, and server dependencies

| Tool | Role | Key limitation |
| --- | --- | --- |
| [altsign-cli](https://github.com/xhzq233/altsign-cli) | Provision and re-sign .app/IPA through free Apple Account | macOS 12+, Command Line Tools and OpenSSL 3; not itself a background refresher |
| [node-applesign](https://github.com/nowsecure/node-applesign) | Re-sign IPA archives in Node.js CLI/app workflows | Requires valid signing identity and provisioning files |
| [IPAID](https://github.com/shplash/IPAID) | Edit IPA bundle identifier and metadata | **Does not replace** installation and signing |
| [ipa-extract-info](https://github.com/nowsecure/ipa-extract-info) | Extract an IPA's Info.plist | Metadata inspection only |
| [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server) | Self-host Anisette identity headers for supported signers | Depends on Apple's changing authentication services; see upstream issues |
| [omnisette-server](https://github.com/SideStore/omnisette-server) | SideStore Anisette v1/v3 wrapper | A service component, not an IPA installer |
| [libplist](https://github.com/libimobiledevice/libplist) | Parse Apple property lists | Library, not a sideloading end-user interface |
| [libusbmuxd](https://github.com/libimobiledevice/libusbmuxd) and [usbmuxd](https://github.com/libimobiledevice/usbmuxd) | Communicate with devices via USB | Transport libraries/services do not grant signing authorization |
| [ios-deploy](https://github.com/ios-control/ios-deploy) | Mac command-line install/debug | Older tooling; verify support for your iOS/device |
| [cyan / pyzule-rw](https://github.com/asdfzxcvbn/pyzule-rw) | Edit IPA metadata and inject authorized patches/tweaks | Fakesign or repackaging is **not** a trusted installable signature; run signing step separately |
| [SideStore Anisette server list](https://github.com/SideStore/anisette-servers) | Community list of recommended Anisette services | Server inclusion/uptime does not guarantee privacy or auth-token safety |
| [StikJIT](https://github.com/StikDebug/StikJIT) | Developer library to integrate JIT | Requires compatible target app and JIT transport; not a user-facing installer |

### Local signing versus remote signing: where secrets go

| Workflow | Where signing happens | What may be exposed | Recommended precautions |
| --- | --- | --- | --- |
| Desktop or on-device local signer (e.g. Feather or IPASIGN) | Your own device/computer | Local `.p12`, private key, profile, possibly Apple Account credentials | Use an official build, OS-protected credential store, and a separately scoped signing identity |
| **Your own** web signer (e.g. IPA Signer, SignTools) | Server that you control | Uploaded IPA, signing profile, private key and server-side logs | Private network/authentication; restrict uploads/storage, avoid public exposure and delete temporary assets |
| **Third-party** hosted signer (e.g. Purple Installer or Feather Installer's backend) | **Someone else's server** | Your signing certificate, `.p12` password, provisioning profile and potentially the uploaded IPA | Prefer not to use for personal production keys; do not treat HTTPS or a public front end as proof of backend trust |
| Source browser (e.g. iOS Hub, ShrubLibrary) | No signing implied | Third-party metadata, app links and optionally browsing identifiers | Verify upstream release signatures, provenance, licensing and unexpected certificate requests |

A `.p12` is a **portable copy of a private signing identity**. Its password is not the same as an Apple Account password, but handing over both the file and password can enable someone else to sign with that identity until revocation/expiry.

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

A JIT tool successfully connecting to a phone does not prove that an emulator or other target app can run JIT. Modern versions also require the **target application** to support applicable JIT allocator/debugger paths; see [StikJIT integration](https://github.com/StikDebug/StikJIT/blob/main/INTEGRATION.md). App support changes between iOS revisions. The [SideStore JIT guide](https://docs.sidestore.io/docs/advanced/jit) maintains current caveats. [StikDebug](https://github.com/StikDebug/StikDebug) and [SideJITServer](https://github.com/nythepegasus/SideJITServer) use different routes; always follow the chosen tool's latest prerequisites.

### On-device signing is not automatic 7-day renewal

Feather, Ksign, SwiftIPA, BatSign, EnSign, ForgeSign and similar apps sign with certificates you supply. A valid signing certificate does not automatically grant Apple Account free provisioning or sideloaded app refresh. In-app update-checking, re-signing, provisioning-profile renewal, and unattended installation are **different features**. Confirm each separately before promising uninterrupted use.

### App source feeds are not installers

- [SideStore Official Source](https://github.com/SideStore/apps.json) is maintained by the SideStore team; the [Community Source](https://github.com/SideStore/Community-Source) has separate submission criteria.
- [GithubStore](https://github.com/yazdipour/GithubStore) builds a source using selected GitHub Releases. Its optional edit UI has no authentication; leave it disabled except on a trusted private network.
- [TeleStore](https://github.com/yazdipour/TeleStore) reads Telegram via an account session. Restrict server access, protect Telegram API credentials and keep the source limited to apps you can legally distribute.
- Online source browsers (including [iOS Hub](https://github.com/CaseyCZ/iOS-Hub) and [ShrubLibrary](https://github.com/ShrubHub-iOS/ShrubLibrary)) gather **third-party app metadata**. Successfully fetching a Source JSON, or presenting a green availability indicator, is not a malware/rights audit.

### Self-hosted services and credential boundaries

- **AltKeeper and Sideloop** both involve a home host, but AltKeeper's AltServer compatibility mode and its separate unattended profile-renewal mode are distinct operations. Sideloop's documented model re-signs and reinstalls apps when the device is reachable; it requires an unlocked phone during re-signing.
- **Anisette** implementations provide Apple-authentication metadata; they do **not** replace signing, provisioning or installation. Apple can change these protocols without advance notice. Avoid sending Apple passwords, session tokens, .p12 files or pairing records to an untrusted service.
- A public signing website that asks for your **private certificate** or .p12 password is a qualitatively different trust boundary from a client that signs locally. Evaluate who can retain your certificate before uploading.

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

Back to [Awesome iOS Sideloading](README.md). See also [research scope and decisions](RESEARCH_NOTES.md).
