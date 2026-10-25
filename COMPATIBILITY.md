# Compatibility and setup notes

> An intentionally compact companion to [README.md](README.md). The main list stays easy to scan; this document records setup differences, signing constraints, and known limitations.

**Last reviewed:** 2026-10-25. **Legend:** `Yes` = feature documented by the maintainer; `Setup` = computer needed for initial pairing/bootstrap; `Varies` = depends on the particular installation method, certificate, or firmware; `—` = not applicable. **Not a hands-on test certification.**

## Choose an installation workflow

| Project | Primary use | Computer / host | Signing or refresh model | Important caveat |
| --- | --- | --- | --- | --- |
| [AltStore Classic](https://github.com/altstoreio/AltStore) | Install and update IPA files | Windows/macOS AltServer, **or configured Remote AltServer** | Personal Apple Account; normal profile renewal | **AltStore Classic 2.3.1 (21 Oct 2026)** documents fixes for `-80045`, 2FA and background refresh; Classic 2.3 requires iOS 17.4+ |
| [SideStore](https://github.com/SideStore/SideStore) | Install/refresh on device | Setup / pairing path varies | Personal Apple Account; on-device renewal with local VPN transport | **0.6.4 and earlier documented as unable to sign in**; 0.7.0-alpha addresses older 503 errors but October sign-in may still fail. Check nightly and official issues |
| [AltLoad](https://github.com/mirazbakis/AltLoad) | Set up AltStore/SideStore/LiveContainer from iPhone | iOS **27+** self-pairing claimed; iOS 18–26 needs pairing record created on PC | Free Apple Account / LocalDevVPN | Early-stage; ordinary sideloading requires first installing AltLoad, and shared-certificate/DNS bootstrap is not equivalent to personal signing |
| [Scarlet](https://usescarlet.com/) | On-device IPA installation, app sources, and tweak injection | Depends on installation mode (direct, computer, own certificate) | Shared certificate, personal developer account, or owned signing assets | Proprietary; direct/shared-certificate route can be revoked or unavailable |
| [MultiStore](https://github.com/lungustefan/MultiStore) | Manage SideStore installs across Apple IDs | Initial setup/pairing via iloader or similar | Per-app signing identity, refresh grouped by Apple Account | Community fork; multiple accounts do **not** remove per-account or per-device Apple limits |
| [Sideloadly](https://sideloadly.io/) | Direct desktop installation | Windows/macOS | Free/paid account; optional desktop auto-refresh | Needs running desktop for automated refresh; JIT is version-restricted |
| [IPASIGN](https://github.com/CyberTKR/IpaSigner) | Desktop IPA re-signing and profile setup | macOS + Qt 6/Xcode command-line tools | Locally supplied signing identity, optional App Store Connect API keys | Early-stage; verify handling of privileged developer credentials and artifacts |
| [IPAForge](https://github.com/IPAForge/ipaforge) | Cross-platform SideStore install, IPA signing and refresh | Windows/macOS/Linux (upstream release assets) | Free Apple Account, SideStore pairing and desktop refresh | **0.1.0-alpha.7 prerelease**; not independently tested, unsigned/not-notarized desktop installers may trigger OS warnings. Compare diagnostics and actual refresh separately |
| [Feather Installer](https://github.com/yodaluca23/Feather-Installer) | Browser-assisted Feather bootstrap | Browser + **third-party ipasign.cc backend** | Uploaded `.p12`, profile and password | **Sensitive signing materials sent to third-party API**; use only with an appropriately isolated identity |
| [Purple Installer](https://github.com/username252510/Purple-Installer) | Hosted web bootstrap for Feather/Ksign/SideInstaller | Browser + **third-party Daisuke Signer backend** | Uploaded `.p12`, profile and password | Browser local storage does not prevent material being sent to remote signer |
| [iloader](https://github.com/nab138/iloader) | SideStore and IPA setup | Windows/macOS/Linux | Installer and pairing manager | A setup tool; not an independent background refresh service |
| [Impactor](https://github.com/claration/impactor) | Cross-platform sideloading | Desktop (see upstream builds) | Depends on signing mode | Check available releases and platform instructions |
| [althea](https://github.com/vyvir/althea) | GUI for AltServer-Linux | Linux desktop or supported ARM host | AltServer-Linux and Apple Account | Upstream marks project early-stage; do not assume support for every new iOS |
| [Splice](https://github.com/franklintra/splice) | Desktop sideloading and scheduled refresh | Linux, Windows or macOS (consult releases) | Apple Account re-sign/reinstall | Maintained fork of Sideloader; automatic refresh claims not independently tested |
| [ModStaller](https://github.com/Crafttino21/ModStaller) | Install/refresh IPAs; experimental JIT and tvOS | Linux or Windows host; USB pairing initially | Free/paid Apple Account, desktop-driven renewal | New experimental tool; iOS 27/tvOS/JIT are upstream claims, not independent test results; Android-host version is **not implemented** |
| [ipaverse](https://github.com/bahattinkoc/ipaverse) | App Store downloads, IPA inspection and installation | **Apple Silicon macOS 14.6+** | Personal signing certificate/profile for DRM-free IPA | FairPlay-encrypted App Store downloads are **not directly re-signable** |
| [Feather](https://github.com/claration/feather) | On-device IPA sign and install | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate expiry/revocation still applies |
| [Ksign](https://github.com/Nyasami/Ksign) | On-device IPA signing | No desktop for ordinary certificate-based use | Your signing certificate/profile | Certificate provenance matters |
| [SwiftIPA](https://github.com/xsxs18-dev/SwiftIPA) | On-device re-sign, IPA edit and OTA installation | iPhone/iPad (iOS 16+ claimed by upstream) | Your .p12 and provisioning profile | Early-stage; author documents optional public relay **for manifest metadata** |
| [BatSign](https://github.com/8yy/BatSign) | On-device signing, background updates | iOS 16+ claimed by upstream | Certificate-based | Automated installs/notifications are upstream claims; test on real devices and firmware |
| [ForgeSign](https://github.com/Mesutcydev/ForgeSign-iOS) | On-device IPA re-signing and OTA install | iOS device | Your .p12 and profile | Check releases and supported firmware |
| [EnSign](https://github.com/cc158999/EnSign) | On-device signing and update workflow | iPhone/iPad | Certificate-based | Check upstream docs and independent security evidence |
| [LiveContainer](https://github.com/LiveContainer/LiveContainer) | Run guest apps inside a host | Host app must first be installed via **supported signer** | Host's signing/refresh applies | Official guide rejects Sideloadly, i4/3u Tools, NB Tool and most online signers; standalone needs AltStore 2.2.1+ or SideStore 0.6.2+ |
| [TrollStore](https://github.com/opa334/TrollStore) | Persistent installation | Depends on firmware-specific bootstrap | Exploit-based; not 7-day personal provisioning | Official supported firmware ranges only |
| [SideInstaller](https://github.com/FrizzleM/SideInstaller) | On-device SideStore bootstrap | On iOS 27+: no PC path; earlier: pairing-file prerequisites | SideStore/free-account workflow after install | Author documents iOS 17.4+, with different pairing requirements |
| [AltKeeper](https://github.com/BartolomeoRusso9/altkeeper) | Self-hosted AltServer and renewal | Always-on home machine; USB pairing once | AltStore protocol plus optional unattended profile renewal | **Experimental**; unattended mode stores account password on host |
| [Torch](https://github.com/trollzem/torch) | macOS automated IPA signing/reinstallation (iOS/iPadOS/tvOS) | macOS host that can reach/pair devices | Free Apple Account, six-day refresh claimed by author | Small experimental project; inspect bootstrap scripts and local credential handling before using |
| [Sideloop](https://github.com/filippofinke/sideloop) | Scheduled re-sign/reinstall over Wi-Fi | Linux/macOS Docker server; pairing initially via USB | Free Apple Account with AltServer-Linux | Device must be unlocked, nearby, and on same Wi-Fi during refresh; 2FA and credentials on server |
| [AltDaemonModern](https://github.com/emp0ry/AltDaemonModern) | Jailbroken on-device refresh/signing | Rootless jailbreak and compatible package setup | Apple Account / AltDaemon | Requires jailbreak; **not** equivalent to SideStore on jailed devices |
| [SideStore Auto Refresh](https://github.com/NRG-Wardog/sidestore-auto-refresh) | Community automatic-refresh workflow | Device/setup-dependent | Free Apple Account and SideStore-based process | Check upstream installation method and restrictions |
| [SignTools](https://github.com/SignTools/SignTools) | Self-hosted signing web UI | Service host + macOS builder | Signing certificates and profiles | Builder/signing infrastructure needed |
| [SignTools GitHub Actions Builder](https://github.com/maxexcloo/signtools-builder) | SignTools private build worker on GitHub Actions | GitHub macOS runner + Tailscale + private SignTools server | Reuses Apple session and SignTools signing credentials | Does **not** provide a standalone app installer; secrets/session and privileged GitHub Actions access require review |
| [IPA Signer](https://github.com/aoyn1xw/ipa-signer) | Self-hosted web/API signing + OTA download | Linux/macOS + Node.js 22+ or Docker | Provided certificate, profile and IPA uploaded to the server | **Keep behind authentication/private network**; web-signing upload endpoint is sensitive |
| [GithubStore](https://github.com/yazdipour/GithubStore) | Self-hosted AltStore source generated from GitHub Releases | Docker host | Feeds original GitHub IPA release URLs | Optional configuration UI has **no authentication**; scope to trusted upstream repos |
| [App Distribution Server](https://github.com/significa/app-distribution-server) | Internal OTA/QR distribution of already signed IPA or APK builds | Your Docker host | **Does not sign** IPAs or register devices | Default `UPLOADS_SECRET_AUTH_TOKEN` is `secret`; change it, enforce HTTPS and access control before deploying |
| [TeleStore](https://github.com/yazdipour/TeleStore) | Self-hosted AltStore source from Telegram channels | Docker host + Telegram API/session | Telegram-channel IPA assets | Protect Telegram session; only distribute apps with permission |
| [IPA Signer Telegram bot](https://github.com/lxdxrx/ipa-signer) | zsign IPA signing and OTA delivery through private Telegram bot | Docker host + Telegram Bot API and local Bot API server | Uploaded certificate/profile and IPA or source URL | **Sensitive identity risk**: .p12/profile and sometimes password pass through bot/chat infrastructure. Restrict user IDs, rotate secrets, and avoid your primary key |
| [AltServer-Linux](https://github.com/NyaMisty/AltServer-Linux) | AltServer-compatible Linux daemon | Linux host | Apple-account-based signing | Older project; check recent issues/releases first |
| [atvloadly](https://github.com/bitxeno/atvloadly) | Apple TV sideloading | Linux/OpenWrt or other supported host | Device and account dependent | tvOS support is separate from iOS |

## Signing, metadata, and server dependencies

| Tool | Role | Key limitation |
| --- | --- | --- |
| [altsign-cli](https://github.com/xhzq233/altsign-cli) | Provision and re-sign .app/IPA through free Apple Account | macOS 12+, Command Line Tools and OpenSSL 3; not itself a background refresher |
| [AltSign](https://github.com/rileytestut/AltSign) | Original Apple-account/re-signing framework used in sideloading ecosystem | Library (CocoaPods / iOS), not an installation UI |
| [SideSign](https://github.com/SideStore/SideSign) | SideStore-maintained Swift framework for developer account API, provisioning, and IPA resigning | Library; Apple auth APIs can change without public notice |
| [CodeSignKit](https://github.com/mahee96/CodeSignKit) | Swift Mach-O/code-signing and recursive app-bundle signing | Does not provision Apple accounts by itself; review AGPL terms |
| [AnisetteKit](https://github.com/mahee96/AnisetteKit) | On-device Anisette generation/ADI emulation across Apple platforms | Cryptographic headers alone do not guarantee successful Apple sign-in |
| [GSACryptoKit](https://github.com/mahee96/GSACryptoKit) | SRP-6a authentication and cryptography helpers | Protocol library, not a standalone IPA signing or installer service |
| [node-applesign](https://github.com/nowsecure/node-applesign) | Re-sign IPA archives in Node.js CLI/app workflows | Requires valid signing identity and provisioning files |
| [IPAID](https://github.com/shplash/IPAID) | Edit IPA bundle identifier and metadata | **Does not replace** installation and signing |
| [ipa-extract-info](https://github.com/nowsecure/ipa-extract-info) | Extract an IPA's Info.plist | Metadata inspection only |
| [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server) | Self-host Anisette identity headers for supported signers | Depends on Apple's changing authentication services; see upstream issues |
| [omnisette-server](https://github.com/SideStore/omnisette-server) | SideStore Anisette v1/v3 wrapper | A service component, not an IPA installer |
| [libplist](https://github.com/libimobiledevice/libplist) | Parse Apple property lists | Library, not a sideloading end-user interface |
| [libusbmuxd](https://github.com/libimobiledevice/libusbmuxd) and [usbmuxd](https://github.com/libimobiledevice/usbmuxd) | Communicate with devices via USB | Transport libraries/services do not grant signing authorization |
| [ios-deploy](https://github.com/ios-control/ios-deploy) | Mac command-line install/debug | Older tooling; verify support for your iOS/device |
| [go-ios](https://github.com/danielpaulus/go-ios) | Cross-platform device pairing/app installation/diagnostics | Device communication library/CLI; signing generally separate |
| [xtool](https://github.com/xtool-org/xtool) | SwiftPM app build, codesign and deploy CLI on Windows, Linux and macOS | Intended primarily for development workflows, not a catalog/automatic IPA refresher |
| [cyan / pyzule-rw](https://github.com/asdfzxcvbn/pyzule-rw) | Edit IPA metadata and inject authorized patches/tweaks | Fakesign or repackaging is **not** a trusted installable signature; run signing step separately |
| [Sideloadly Monitor](https://github.com/recallsangel/sideloadly-monitor) | macOS launchd status/expiry monitor with Telegram alerts | Reads Sideloadly's internal SQLite database read-only | Can conditionally restart the daemon, not re-sign or redeploy an individual IPA |
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

### IPA discovery does not sign or verify packages

[ryP0](https://github.com/Sami-Wali/ryP0), [ShrubLibrary](https://github.com/ShrubHub-iOS/ShrubLibrary) and [iOS Hub](https://github.com/CaseyCZ/iOS-Hub) are **catalogs/bridges**, not proof that a third-party build is signed, unmodified, or legally redistributable. For ryP0, upstream [release 2.2](https://github.com/Sami-Wali/ryP0/releases/tag/2.2) provides an unsigned IPA; signing/installation still requires a suitable tool.

### Self-hosted signing secrets in chat or CI

- **Telegram bots:** certificate archives sent to a bot can traverse Telegram's infrastructure even if the bot server is self-hosted. Encryption at rest of *passwords on your server* is not end-to-end secrecy for bot uploads. Restrict allowed Telegram users, storage, logs, and backup access; consider a locally run signer rather than a bot for important developer keys.
- **GitHub Actions signing workers:** an Apple `FASTLANE_SESSION`, SignTools authentication key, signing certificate and repository-scoped secrets token are privileged credentials. Use minimal secret scopes, explicit permission boundaries, ephemeral workers and private connectivity. The community [SignTools builder](https://github.com/maxexcloo/signtools-builder) uses Tailscale and documents these requirements.
- **Refresh monitors:** [Sideloadly Monitor](https://github.com/recallsangel/sideloadly-monitor) observes a proprietary app's private database format. Such a monitor can identify problems but does not create new Apple certificates or guarantee 7-day renewal.


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

## Current compatibility snapshots

These are **historical checkpoints dated 25 October 2026**, not a permanent “latest versions” matrix. Always confirm official upstream updates.

| Project | Confirmed upstream reference | Practical interpretation |
| --- | --- | --- |
| **AltStore Classic** | [2.3.1 release notes (21 Oct 2026)](https://github.com/altstoreio/FAQ/blob/main/release-notes/altstore.md) | Fixes for authentication `-80045`, 2FA prompts, background refresh and Remote AltServer handling are documented. AltStore 2.3 raised the minimum to **iOS 17.4** |
| **SideStore** | [0.6.4](https://github.com/SideStore/SideStore/releases/tag/0.6.4) and [0.7.0-alpha](https://github.com/SideStore/SideStore/releases/tag/0.7.0-alpha) | Upstream marks 0.6.4 and earlier `DO NOT USE` due to broken sign-in. 0.7.0-alpha targeted 503 but additional October issues exist; nightlies are **experimental** |
| **LiveContainer** | [3.8.0 release notes](https://github.com/LiveContainer/LiveContainer/releases/tag/3.8.0) and [official install guide](https://livecontainer.github.io/docs/installation) | Standalone requires AltStore **2.2.1+** or SideStore **0.6.2+** to install; official docs specifically **do not support Sideloadly** and most online signers for installing LiveContainer |
| **SideInstaller** | [1.5.0 changelog](https://github.com/FrizzleM/SideInstaller/blob/main/CHANGELOG.md) | Maintainer documents fixes to Apple sign-in after the 12 Oct change; the new solution still requires supported firmware/setup and is not proof of blanket account compatibility |

### Selecting a supported installer for LiveContainer

**LiveContainer is different from a generic IPA.** Its bundled frameworks, SideStore integration, app extensions and certificate-import process require the [officially supported installation paths](https://livecontainer.github.io/docs/installation). Use **iloader or Impactor** for the LiveContainer+SideStore bundle, or a sufficiently recent **AltStore/SideStore** for the standalone app. Check the [standalone setup guide](https://livecontainer.github.io/docs/installation/standalone) for JIT-less certificate import and diagnostic checks. A successful one-time install with some other signer does not imply future refresh, app extensions or nested frameworks will work.

## October 2026 Apple ID / Anisette disruptions

**Snapshot: 25 October 2026.** Several third-party sideloading tools reported Apple-authentication failures from around **13–15 October 2026**. AltStore 2.3.1 subsequently documented fixes for its own `-80045`/2FA/refresh workflow, whereas SideStore's open reports and experimental builds require separate treatment. These are **upstream community reports**, not a proof of universal Apple ID bans, and should not be treated as a reason to repeatedly retry a password or replace an identity blindly.

| Symptom | Primary source | What is known |
| --- | --- | --- |
| `-80045` during SideStore login | [SideStore issue #1647](https://github.com/SideStore/SideStore/issues/1647) | Multiple October reports across build and anisette combinations; may involve identity/client mismatch, unavailable authentication paths or different errors surfaced with the same code |
| HTTP `503`, failed 2FA, unable to connect to iCloud | [SideStore community discussion #1666](https://github.com/orgs/SideStore/discussions/1666) | Temporary Anisette and client-information adjustments vary across versions and can stop working after server-side Apple changes |
| A proposed broader SideStore patch | [SideStore PR #1683](https://github.com/SideStore/SideStore/pull/1683) | **Open when reviewed**; do not imply that an unmerged PR is in the stable release |
| macOS 27 AltServer login errors | [kimziro/altserver-macos27-anisette-fix](https://github.com/kimziro/altserver-macos27-anisette-fix) | **Unofficial, ad-hoc signed** macOS 27/Apple Silicon compatibility package. Author reports a successful USB install; refresh and remote operation are not independently established |

**Safer troubleshooting order:** check the exact tool version and [official project releases](https://github.com/SideStore/SideStore/releases), read active [SideStore issues](https://github.com/SideStore/SideStore/issues) and [official Anisette server directory](https://github.com/SideStore/anisette-servers), avoid repeated failed logins, and protect pairing/session records. Error codes alone do not confirm an account ban. Prefer verified upstream fixes over arbitrary identity strings from old comments or unsigned binary mirrors.

### Limits of multi-account setups

Multiple Apple Accounts can provide distinct **App ID quota and certificates**, and [MultiStore](https://github.com/lungustefan/MultiStore) can associate different apps with each. That **does not necessarily increase the device-wide number of simultaneously active free-provisioned app slots**. The three-app limit is generally enforced on the device; do not assume three installed apps *per Apple Account*. LiveContainer's guest apps have separate compatibility/security tradeoffs.

## Additional developer tooling reviewed 25 October 2026

These tools serve very different stages of the sideloading workflow; do not choose an IPA downloader when you actually need an installer or a profile refresher.

| Project | Role and host | Actual signing/install scope | Major limitation |
| --- | --- | --- | --- |
| [KeepAlive](https://github.com/oli-zr/keepalive) | macOS 14+, Xcode 15+ menu-bar scheduled **rebuild** of projects you own | Builds with `xcodebuild` and installs via `devicectl` | **Not an arbitrary IPA signer**; Mac/Xcode and a reachable registered device required. App entitlements remain limited by Apple Personal Team |
| [SignTools Builder](https://github.com/SignTools/SignTools-Builder) | Official standalone macOS worker for self-hosted SignTools | Signs apps requested by SignTools server | Upstream has **no native HTTPS** and warns about possible remote command execution by other reachable machines; run on a dedicated Mac behind authenticated TLS/private network |
| [AltGen](https://github.com/bebound/AltGen) | Python 3.10+ CLI; GitHub Releases → AltSource `apps.json` | Generates/merges repository JSON; **no IPA signing/install** | Release and IPA URLs are upstream inputs; operator still controls trust, license and hosting |
| [IPATool GUI](https://github.com/a23bc/ipatool-gui) | Windows/macOS/Linux GUI wrapping `majd/ipatool` | Downloads App Store packages acquired by user's Apple Account; **no re-signing** | FairPlay-encrypted downloaded IPAs are not automatically re-signable; private Apple protocols and device compatibility change |
| [Appium resigner](https://github.com/appium/resigner) | Go CLI/library on Windows/macOS/Linux | Local re-signing and inspection of `.ipa` / `.app` for Appium/WebDriverAgent | **Maintainer warns not to use for production signing**, requires appropriate `.p12` and provisioning profiles |
| [iOS Developer Toolkit](https://github.com/hideouts-io/iOS-Developer-Toolkit) | macOS PySide6 GUI built around `pymobiledevice3` | Device diagnostics, Developer Disk Images, IPA inspection and installation **when already eligible/signed** | Not a sideload signing/provisioning service, not a jailbreak or sandbox escape; sensitive backup/device evidence requires controlled storage |
| [IpaDownloadTool](https://github.com/SmileZXLee/IpaDownloadTool) | iOS app for handling OTA `itms-services` and distribution manifests | Resolves/downloading IPAs for authorized testing and inspection | Does **not** remove signature/DRM or expand install eligibility; some OTA distribution links may reveal UDID or private app access |

### Separate four workflows before choosing a tool

1. **Acquire IPA:** `ipatool` and IPATool GUI may download **FairPlay-encrypted** App Store purchases; an authorized private OTA package source is another route. Neither gives rights to redistribute.
2. **Sign or re-sign IPA:** Appium resigner, AltSign/SideSign, zsign and similar tools need an appropriate signing identity/provisioning profile and correctly signed embedded extensions.
3. **Install and refresh:** iloader, SideStore, AltStore, KeepAlive and SignTools have different installation mechanisms and **very different** background renewal capabilities. KeepAlive rebuilds **your own Xcode source**; SignTools serves **prebuilt IPAs** after remote signing.
4. **Publish a source:** AltGen produces `apps.json`, whereas GithubStore dynamically serves sources and App Distribution Server hosts already-signed download files. Those tools are not substitutes for profile creation, encryption removal, or device signing.

#### Safeguards for developer machines

Keep certificates, `.p12` passwords, Apple Account sessions and iOS device pairing records outside published repositories and public issue logs. A Mac acting as a SignTools builder should use a protected private network and TLS termination; see the project's own warning on remote code execution. Downloaded App Store archives can be bound to an Apple Account through FairPlay even if the archive has an `.ipa` extension.

## Apple TV, Vision Pro, restoration and app-analysis tools (reviewed 25 October 2026)

The three device families below differ in **pairing**, **on-device vs hosted refresh**, and **JIT**. A list of supported platforms in an upstream README is not a physical-device certification. See [further research and release evidence](RESEARCH_NOTES.md#seventh-research-pass-tvos-visionos-and-offloaded-app-restoration-25-october-2026).

| Tool | Requirements and workflow | Renewal / installation | What is and is not verified |
| --- | --- | --- | --- |
| [Apparition](https://github.com/illixion/Apparition) | Initial install via desktop on Windows/macOS/Linux; iPhone/iPad USB pairing or TV/Vision Pro network pairing; subsequent on-device app uses LocalDevVPN or a companion | On-device IPA signing, installation, refresh and newer-firmware JIT are **maintainer claims** | Early project with [v0.3.2 releases](https://github.com/illixion/Apparition/releases/tag/v0.3.2); JIT on modern visionOS/iOS needs version-and-app-specific evaluation. Background operation and VPN/location permissions should be reviewed |
| [Lodestar](https://github.com/asroya/lodestar) | **macOS Apple Silicon**, own Apple Account; iPhone USB or previously paired Apple TV 4K | **Manual one-click refresh**, no unattended auto-refresh | Maintainer [v1.0.0](https://github.com/asroya/lodestar/releases/tag/v1.0.0) reports physical iPhone USB and paired Apple TV install; first pairing by TV code, SMS 2FA and refresh have explicitly limited/no hardware verification |
| [Catapult](https://github.com/byrvr/catapult) | macOS 14+, local SwiftUI/Python backend, Apple developer account; optional encrypted IPA vault synchronized between Macs | Offers scheduled refresh before free provisioning expires | [v0.4.2 macOS DMG](https://github.com/byrvr/catapult/releases/tag/v0.4.2); cross-device sync is **opt-in**, and exposing IPA blobs or signing sessions to a cloud folder must be evaluated independently |
| [tvsign](https://github.com/esalwey/tvsign) | Always-on **Windows 10/11 or Docker on Linux, Raspberry Pi/NAS**; free Apple Account; Apple TV/iPhone/iPad must be reachable across local network | Signs/installs, monitors GitHub releases and attempts renewal before 7-day expiry | [v1.0.1](https://github.com/esalwey/tvsign/releases/tag/v1.0.1); Docker Desktop on Windows/macOS is **not** the documented supported host, and mDNS across VLANs may require addressing/network adjustments. Don't expose auth UI to the Internet |
| [TapOk IPA Tools](https://github.com/TapOk38/tapok-ipa-tools) | Experimental Windows Store downloader plus separate **Windows or Android USB installer** | Installs IPA that meets device's existing code-signing requirements; does **not** make unsigned apps installable | [suite-v1.0.0-beta.5](https://github.com/TapOk38/tapok-ipa-tools/releases/tag/suite-v1.0.0-beta.5), very little independent testing; Android host is notable but should be validated on exact phone and iOS build |
| [AppRestore](https://github.com/J3ckJ/AppRestore) | Windows/macOS computer, USB cable and authorized Apple Account ownership or existing eligible IPA | Attempts to restore **offloaded or removed** App Store apps, often without needing a new developer signing process | [v0.4.0](https://github.com/J3ckJ/AppRestore/releases/tag/v0.4.0) offers GUI/CLI artifacts. **No FairPlay decryption/DRM bypass**, and an account cannot simply reinstall an app it never obtained or an app unavailable to its license |
| [AppInspect](https://github.com/iCrazeiOS/AppInspect) | Windows/macOS/Linux offline Electron workbench for IPA, DEB, Mach-O, app extensions and frameworks | **Read-only static inspection**, no actual signing, installing, JIT or Apple authentication | Useful for examining entitlements, symbols, Info.plist and potential security findings. Static heuristics do **not** prove an IPA is malware-free. No published GitHub releases at review time |
| [SignTools CI](https://github.com/SignTools/SignTools-CI) | GitHub Actions/Semaphore template in a **private repository**; connects to self-hosted SignTools | Remote worker signs requested apps; signing profile managed by SignTools | **Official SignTools** implementation, but upstream explicitly states that **free Apple developer accounts are unsupported from SignTools 3.0 onward**. Privileged CI API tokens/sessions require minimal access scope |

### Restoration is not sideloading

**Offloaded App Store app:** the icon may remain but the binary is gone. AppRestore first asks the device/App Store to restore it; if Apple cannot serve it, an already acquired and valid IPA may be needed. An arbitrary downloaded IPA from a different Apple ID does not guarantee installation.

**Developer-signed IPA:** separate from an App Store app and typically subject to seven-day free developer provisioning. Updating its contents or signing a new bundle is not equivalent to redownloading an offloaded Store app.

**Inspecting before installation:** AppInspect can show an embedded bundle identifier, app extensions and signature entitlements. It does not independently verify source provenance, runtime behavior, Apple authorization, or DRM status.

### Apple TV pairing, renewals and JIT

- **Paired vs first-time pairing:** many tools can reuse an existing tvOS pairing record even when PIN-based first-time pairing is untested; do not advertise both as verified.
- **Renewal:** manual one-click re-install (Lodestar), desktop-driven scheduled refresh (Catapult), Docker/Windows hosted scheduled renewal (tvsign), and on-device refresh (Apparition) are distinct capabilities.
- **Modern JIT:** attaching a debugger once is **not** sufficient for all apps on iOS/tvOS/visionOS. Treat on-device JIT claims as specific to the chip, OS build, emulator and implementation, not as an automatic benefit of installing through a certain app.
- **Auth/session isolation:** passwords, Anisette provisioning blobs, pairing records, app-signing certificates and local web admin passwords must be protected even when a tool is self-hosted.

## Emerging signers, Fedora installation and TestFlight (reviewed 25 October 2026)

This snapshot distinguishes **published GitHub artifacts**, **maintainer-advertised capability**, and **independently verified device compatibility**. Publishing a tagged IPA or Windows executable only verifies that an artifact exists, not that its signing or refresh workflow passes on current devices.

| Project | Platform / distribution | Actual purpose | Trust and compatibility notes |
| --- | --- | --- | --- |
| [SideKick](https://github.com/huzaifah1530-bot/SideKick) | iOS 18+ target; [v0.10.0 prerelease](https://github.com/huzaifah1530-bot/SideKick/releases/tag/v0.10.0) with `SideKick.ipa` and source archive | SideStore-derived signing/installation with GitHub release and Actions artifact updates, IPA library and LiveContainer guest-app metadata | Early release explicitly marks **advanced features in progress**; SideStore engine, LocalDevVPN and Apple Account restrictions still apply; no independent hands-on validation |
| [SignOs](https://github.com/ihateios/SignOs) | iOS on-device; [v1.0.0 signed? no—IPA artifact](https://github.com/ihateios/SignOs/releases/tag/v1.0.0) | Feather-based IPA signer claiming background updates, cloning and renewal | Background **silent installation** is upstream marketing, not established platform capability. App extensions, iOS prompts, entitlement limits and certificate revocation still apply |
| [DenizSigner](https://github.com/LaFAirs/DenizSigner) | **Windows x64**; [v0.1.0](https://github.com/LaFAirs/DenizSigner/releases/tag/v0.1.0) portable EXE, setup EXE and MSI | Local USB IPA signing/install, SideStore/LiveContainer setup and certificate/account UI | Prototype v0.1.0. Uses Apple auth plus third-party Anisette headers. Local-first privacy claims and network allowlist are **author assertions**, not an independent security review; Windows signing is not yet a publisher-authenticated binary |
| [iloader Fedora COPR](https://github.com/anudeepd/iloader-fedora-copr-ci) | **Fedora x86_64**, optional [community COPR package](https://copr.fedorainfracloud.org/coprs/anudeepd/iloader/) | Automated repackaging of upstream iloader RPM, checking recorded upstream SHA256 before submission | **Not an official Fedora package** and not built from source in COPR. Still trust upstream release provenance, package maintainer, and COPR signing |
| [Awesome TestFlight Links](https://github.com/pluwen/awesome-testflight-link) | Apple-hosted TestFlight beta invitation links for iOS/iPadOS/macOS/tvOS/visionOS | Discover currently reported beta invitations, not IPA archives | **Not a sideloader**: Apple TestFlight handles beta installation/signing, free personal-development limits do not apply in the same way. Invite capacity, validity and listing statuses can become stale |

### Why TestFlight is separate from IPA signing

**Apple TestFlight** invites are author-controlled beta distribution. An Apple-hosted invite can install an authorized beta through the TestFlight app without uploading a personal `.p12` or using an arbitrary IPA signer. It cannot sideload a locally modified IPA or replace AltStore/SideStore for an app not enrolled by its developer. Community lists may contain expired or full programs.

### October 2026 Apple authentication reports: reproducibility boundaries

- [SideStore PR #1683](https://github.com/SideStore/SideStore/pull/1683) remained **open/unmerged on 25 Oct 2026**. Never describe its new login code as available in a stable release before upstream confirmation.
- In [r/SideStore](https://www.reddit.com/r/SideStore/comments/1x4ag7b/apple_account_logins_no_longer_working_sidestore/), [r/sideloaded](https://www.reddit.com/r/sideloaded/comments/1xbht4m/sidestore_sign_in_not_working/) and [r/sideloading](https://www.reddit.com/r/sideloading/comments/1xcsy5q/fix_for_error_80045_80046_and_app_closing_when/), affected users report `-80045`, `-80046`, HTTP 503 and inconsistent Anisette/pairing outcomes. Posts dated **12–24 October** conflict about server selection and client headers.
- Error codes **do not establish an Apple Account ban**. Different failures can look alike: Anisette provisioning, Apple client identity, an invalid pairing file, blocked OTP/2FA, profile issuance or account state. Prefer current official releases and clearly dated maintainer issue reports to copying static identity strings.
- Avoid publishing any Apple ID password, OTP, pairing record, signing `.p12`, Apple session, or Anisette provisioning blob in GitHub Issues or public forum threads.

## October 2026: App Store acquisition, device installation and Anisette patch scope

**Last rechecked 25 October 2026.** These tools are not interchangeable. "Download IPA from the App Store" often means obtaining a **FairPlay-encrypted** archive tied to an account. "Install IPA" generally means installing a **previously signed and eligible** package. "Sign IPA" requires your own certificate and provisioning entitlement.

| Tool | Upstream snapshot and host | What it does | Critical limitations |
| --- | --- | --- | --- |
| [ipatool (official)](https://github.com/majd/ipatool) | [v2.7.0, 9 Oct 2026](https://github.com/majd/ipatool/releases/tag/v2.7.0); Windows/macOS/Linux/iOS | Apple Account-authorized search/purchases/version selection and IPA/PKG download | **2.4.0+** integrated SAP-based authentication; many pre-August 2026 articles asserting official ipatool authentication is broken are outdated. App Store IPAs can retain FairPlay encryption |
| [ipatool-rs](https://github.com/Kosthi/ipatool-rs) | [v0.1.8, 30 Aug 2026](https://github.com/Kosthi/ipatool-rs/releases/tag/v0.1.8); Rust CLI/TUI | Independent App Store API client with Apple login/2FA and resumable downloads | Its README comparison claims Go ipatool auth is broken, but official Go ipatool released [v2.4.0+](https://github.com/majd/ipatool/releases) SAP fixes; **do not repeat that outdated claim**. Not a signing tool |
| [Ferrie](https://github.com/leo1394/homebrew-ferrie) | [v0.2.8, 22 Oct 2026](https://github.com/leo1394/homebrew-ferrie/releases/tag/v0.2.8); Windows/macOS/Linux | Install compatible pre-signed IPA to a connected device through go-ios / CoreDevice; handles Android packages as well | **No Apple Account login, signing, profile creation or DRM bypass**. Requires trusted device, USB transport and platform device services; replacing an app may fail if signing does not match |
| [iOS IPA Extractor](https://github.com/iw00tr00t/ios-ipa-extractor) | Mac script using Frida for app enumeration, ipatool to download | Lists installed bundle IDs and downloads a new copy **from Apple's CDN**, not from the phone's protected app storage | "Extract" is a misleading shorthand: no app decryption, no automatic signing. Frida enumeration on a non-jailbroken phone may require extra permissions and is not independently validated here |
| [Windows iOS IPA Extractor](https://github.com/MayoMusic/ios-ipa-extractor-win) | [v1.0.0, 21 Oct 2026](https://github.com/MayoMusic/ios-ipa-extractor-win/releases/tag/v1.0.0); Windows 10/11, Python + pymobiledevice3 | Reads installed app identifiers through Apple mobile-device services and downloads authorized copies with ipatool | **Very new/limited independent validation**; App Store packages commonly remain FairPlay encrypted. Windows Apple Mobile Device drivers are required |
| [Fletch](https://github.com/Aknaru404/Fletch) | Experimental iOS/iPadOS 17+ Quiver Launcher fork; GitHub Actions **unsigned IPA** artifacts | Tracks GitHub/GitLab/Codeberg releases, saves IPA and sends it to user's own signing tool | **No signing, installation or JIT**; source repository has no standard GitHub Release at review time; download only from original author |
| [AltServer macOS 27 Anisette Fix](https://github.com/kimziro/altserver-macos27-anisette-fix) | [v1.3.3 prerelease, 23 Oct 2026](https://github.com/kimziro/altserver-macos27-anisette-fix/releases/tag/v1.3.3); Apple Silicon macOS 27 only | Third-party patched AltServer and AltStore Classic 2.3.1 companion targeting specific Anisette `machineID`/client-identity failures | **Not official AltStore**, ad-hoc signed and not notarized; new iPhone USB installation reported tested, **background refresh and Remote AltServer not tested**. Do not assume it fixes `-80046`, HTTP 503 or all Apple sign-in problems |

### Authentication fix provenance and security

- [Official ipatool](https://github.com/majd/ipatool/releases) moved forward with SAP support in v2.4.0 and additional fixes in v2.5.0; by 9 October v2.7.0 was published. [ipatool-sapfix](https://github.com/maksimryabkin/ipatool-sapfix) itself explicitly recommends **moving back to maintained upstream**. A historical workaround can still be useful for a pinned environment but should not be recommended as the default.
- An **unofficial patched AltServer** is privileged software that handles device pairing and Apple authentication flows; verify upstream identity, checksums, code signing and exactly which files are replaced. Use the ordinary macOS Privacy & Security approval path instead of globally weakening OS protections.
- [r/EmulationOniOS](https://www.reddit.com/r/EmulationOniOS/) has [concrete September 2026 pairing/JIT reports](https://www.reddit.com/r/EmulationOniOS/comments/1wkl3gd/it_took_me_6_hours_but_i_got_jit_to_work_on_my/) and conflicting 26.x JIT compatibility discussions. **"JIT available" in an emulator does not prove JIT is active**; check chip, firmware, backend, extension presence and a real device-level execution test.
- Never upload your Apple Account passwords, OTPs, private certificates, provisioning profiles, auth tokens, or pairing records when asking for help on GitHub or Reddit.

## On-device App Store discovery, LiveContainer integration and self-hosted renewals (25 October 2026)

These are **four different distribution and installation models**. A downloaded IPA can remain encrypted and bound to an App Store license; an IPA in LiveContainer does not create a new developer signing identity; a hosting service does not issue a valid provisioning profile for arbitrary devices.

| Project | Workflow / host | Observed release evidence and caveat |
| --- | --- | --- |
| [DLiPA](https://github.com/AhmedBafkir/DLiPA) | On-device iOS 13+ Apple Account App Store search, multiple accounts/storefronts, downloads of available older versions and file sharing | [v1.4 published 3 August 2026](https://github.com/AhmedBafkir/DLiPA/releases/tag/v1.4), `DLiPA_v1.4.ipa`. Its README warns about **missing automatic updates** after direct installation and recommends AirDrop in some cases. Apple licenses, FairPlay and app-version availability are independent constraints |
| [LBox](https://github.com/Lolendor/LBox) | iOS 17.6+ download manager/source browser; selects Files-accessible LiveContainer folder, unpacks IPA into its applications area and opens via `livecontainer://` | [v1.2 IPA published 8 December 2025](https://github.com/Lolendor/LBox/releases/tag/v1.2). **Not a signing engine or a direct unrestricted iOS installer**; first-run bundle metadata errors, file picker permission and guest-app compatibility may block the workflow. Last recorded upstream push Dec 2025; mature or abandoned status unknown |
| [iPhoneLoadly](https://github.com/lemehavit/iPhoneLoadly) | **Debian 13 x86_64** Rust signing daemon, free Apple Account provisioning, one-time USB pairing, subsequent Wi-Fi installs with configurable expiry-triggered renewal | [v0.3.0-alpha.5 published 20 October 2026](https://github.com/lemehavit/iPhoneLoadly/releases/tag/v0.3.0-alpha.5) with Linux archive and SHA256 sidecar. Its README badge lags behind the release version. **Experimental alpha; scheduled job cannot renew if phone is unreachable or the Apple login session requires 2FA** |
| [PGYER CLI](https://github.com/PGYER/pgyer-cli) | Official hosted Pgyer developer build distribution, Node.js 20+, IPA/APK/HAP uploads, invited/password access, CI and MCP automation | GitHub source updated Oct 2026, **no GitHub Releases artifacts at review time**; tool is distributed via `@pgyer/cli` on npm. **Hosted provider receives uploaded IPA and metadata**; API keys and install passwords must be protected; this is not a free-account IPA signer |

### Security boundaries

- **Apple Account/App Store:** DLiPA and `ipatool` operate against Apple's stores. An IPA may be encrypted and restricted to the purchasing account; download and share affordances do not grant license-transfer rights. Older versions may disappear from App Store availability even when a version ID is known.
- **LiveContainer guest installation:** LBox requires explicit Files permission to the correct LiveContainer folder. Unpacking and launching a guest app is different from installing a separately signed app through `installd`; extension, keychain, entitlement and notification behavior may differ.
- **Debian signer:** iPhoneLoadly stores device pairing records and may optionally persist encrypted Apple Account secrets. Prefer its local `127.0.0.1` binding plus the documented authenticated TLS reverse-proxy/SSH tunnel pattern; do **not** expose signing/admin endpoints on public Internet.
- **Commercial hosting:** PGYER is a hosted distribution service. A published IPA still needs correct iOS signature, provisioning/distribution method, device eligibility and the owner's redistribution rights. Sending a production build to a third party is a separate confidentiality decision.

### Better primary-source troubleshooting

[SideStore's own troubleshooting guide](https://docs.sidestore.io/docs/troubleshooting) and [error codes](https://docs.sidestore.io/docs/troubleshooting/error-codes) distinguish VPN/tunnel reachability, pairing file, Apple Account/Anisette services, profile expiry and app-installation issues. Community fixes from [r/SideStore](https://www.reddit.com/r/SideStore/) or [r/EmulationOniOS](https://www.reddit.com/r/EmulationOniOS/) are best treated as **OS- and device-specific bug reports**, not one-size-fits-all fixes. A displayed `JIT available` status is also not proof that JIT actually activated in an emulator.

## Maintenance and evidence

When changing a compatibility claim, include the **device**, **iOS/iPadOS version**, **tool version**, **signing type**, **date**, and a link to upstream documentation, changelog, or reproducible test notes. Add a statement like _not independently verified_ if the change only reflects a maintainer's claim.

Avoid hardcoding latest iOS numbers as permanent project features; devices, regions, certificates, and OS releases change faster than static lists.

Back to [Awesome iOS Sideloading](README.md). See also [research scope and decisions](RESEARCH_NOTES.md).
