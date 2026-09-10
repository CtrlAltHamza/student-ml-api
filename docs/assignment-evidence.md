# Assignment Evidence

## Verified workflow

1. `main` contains the FastAPI service, four tests, Dockerfile, `.dockerignore`, version file, README, CI workflow, and release workflow.
2. `feature/model-metadata` was merged through PR #1 after CI passed.
3. `feature/release-fix` was merged through PR #2 after CI passed. It fixed the GHCR lowercase image-name requirement.
4. `feature/ci-failure-demo` was merged through PR #3 after showing a failing CI run and then passing CI after corrective commits.

## Failure analysis

- Symptom: the health test failed in CI.
- Cause: the deliberate test commit expected application version `9.9.9` while the service returned `1.1.0`.
- Fix: restore the expected `1.1.0` value, remove duplicated editor content, and rerun CI.
- Prevention: keep health metadata assertions in the automated test suite and require the PR CI check before merging.

## Docker build cache

The Dockerfile copies and installs `requirements.txt` before copying `app.py` and `VERSION`. Rebuilding after changing only `app.py` reuses the dependency-install layer and rebuilds only the application layers. A dependency change invalidates the installation layer intentionally.

Validation commands:

```bash
docker build -t student-ml-api:cache-check .
docker build -t student-ml-api:cache-check .
```

The second build reused cached layers in Docker. The same ordering is used by the GitHub CI build.

## Registry and reproducibility

GHCR contains `v1.0.0`, `v1.1.0`, `latest`, and a commit-SHA image tag. The release image includes OCI labels for application version, source, commit, and build date. The image can be pulled and run in another environment without rebuilding:

```bash
docker pull ghcr.io/ctrlalthamza/student-ml-api:v1.1.0
docker run --rm -p 8000:8000 ghcr.io/ctrlalthamza/student-ml-api:v1.1.0
```

## Rollback

Use `ghcr.io/ctrlalthamza/student-ml-api:v1.0.0` to roll back from `v1.1.0`. This changes only the deployment image tag and does not modify source code or rebuild the image.
