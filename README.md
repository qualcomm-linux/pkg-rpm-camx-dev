# pkg-rpm-camx-dev

RPM packaging for the Qualcomm Linux CamX development headers used by camera
service and GStreamer camera components.

This repository contains RPM packaging rules and scripts for the prebuilt,
target-agnostic CamX usermode API headers. The header payload is provided for
Kodiak camera consumers and contains no compiled libraries or binaries.

The prebuilt CamX camera framework binaries and headers are available from
[QArtifactory](https://qartifactory-edge.qualcomm.com/ui/native/qsc_releases/software/chip/component/camx.qclinux.0.0/).

The `c10s` branch contains the RPM packaging files. The `main` branch contains
repository documentation and workflow support files.

## Repository Layout

| File | Purpose |
|---|---|
| `camx-dev.spec` | Builds the `libcamx-devel` header package. |
| `sources` | SHA-512 checksum for the prebuilt headers archive. |
| `README.md` | Package and repository documentation. |
| `LICENSE.txt` | License for the RPM packaging repository. |

The prebuilt headers archive is not committed to this repository. `Source0` in
the spec points to the QArtifactory release, and the checksum in `sources` is
verified before the RPM is built.

## Package

### `libcamx-devel`

Header-only development package providing the CamX API for camera-service and
GStreamer consumers:

```text
/usr/include/camx-v1
/usr/include/hardware
/usr/include/system
```

The package is `noarch` because it contains headers only. It does not include
runtime libraries, compiled code, or target-specific camera binaries.

## Installation

Install the development headers from the configured CentOS Stream 10
repository:

```bash
sudo dnf install -y libcamx-devel
```

## Updating the Package Version

1. Update `Version:` and `upstream_tag` in `camx-dev.spec`.
2. Update the `Source0` archive reference when the prebuilt headers release
   changes.
3. Regenerate the source checksum:

   ```bash
   sha512sum --tag camx-headers-<version>_arm64.tar.gz > sources
   ```

4. Commit the spec and `sources`, then open a pull request against `c10s`.
5. After the pull request is merged, run `pkg-release.yml` to publish the RPM.

## License

This project is licensed under the BSD 3-Clause License. See [LICENSE.txt](LICENSE.txt) for the complete license text.
