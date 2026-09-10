# student-ml-api

Production-style MLOps exercise for a small FastAPI prediction service.

## API

Run locally with Python:

```bash
python -m pip install -r requirements.txt
uvicorn app:app --reload
```

Endpoints:

- `GET /health` returns service status, application name, application version, and model version.
- `POST /predict` accepts `{"value": 10}` and returns `{"input": 10, "prediction": 20}`.

## Tests and Docker

```bash
pytest
docker build -t student-ml-api:local .
docker run --rm -p 8000:8000 student-ml-api:local
curl http://localhost:8000/health
```

The PR CI workflow installs dependencies, runs tests, and builds the image. It does
not push images. The release workflow publishes `vX.Y.Z` tags to GitHub Container
Registry as `ghcr.io/ctrlalthamza/student-ml-api`, plus `latest` and a commit-SHA
tag. OCI labels record the application version, commit, build date, and source.

The `v1.0.0` image remains available as the rollback target when `v1.1.0` is
deployed. A rollback only changes the deployment image tag; it does not rebuild
or modify application source.

## Git workflow

Work on `feature/*` branches, open a pull request into `main`, wait for CI, then
merge. Direct pushes to `main` should be disabled with GitHub branch protection.

## Deliberate CI failure demonstration

For the required failure evidence, temporarily change the expected health status
in `tests/test_app.py` to an incorrect value, push that commit to a feature branch,
and open a pull request. Restore the expected value in a follow-up fix commit and
wait for the workflow to pass.