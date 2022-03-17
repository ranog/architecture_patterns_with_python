setup-db-test:
	@docker run -d --rm \
		--name architecture \
		-e POSTGRES_PASSWORD=postgres \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_DB=postgres \
		-p 5432:5432 postgres:13-alpine
