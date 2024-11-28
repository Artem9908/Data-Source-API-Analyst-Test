# API Documentation

## GitHub API Endpoints Used

### 1. Search Repositories (Public)

- **Endpoint:** `GET /search/repositories`
- **Description:** Searches for repositories based on a query.
- **Parameters:**
  - `q`: The search keywords.
  - `per_page`: Number of results per page (default: 30, max: 100).
  - `page`: Page number of the results.
- **Documentation Link:** [Search Repositories](https://docs.github.com/en/rest/search#search-repositories)

### 2. List Commits

- **Endpoint:** `GET /repos/{owner}/{repo}/commits`
- **Description:** Retrieves a list of commits for a repository.
- **Parameters:**
  - `per_page`: Number of results per page.
  - `page`: Page number of the results.
- **Documentation Link:** [List Commits](https://docs.github.com/en/rest/commits/commits#list-commits)

### 3. Get Repository Content

- **Endpoint:** `GET /repos/{owner}/{repo}/contents/{path}`
- **Description:** Gets the contents of a repository.
- **Parameters:**
  - `path`: The content path. Defaults to the root if not specified.
- **Documentation Link:** [Get Repository Content](https://docs.github.com/en/rest/repos/contents#get-repository-content)

### 4. Check Rate Limit

- **Endpoint:** `GET /rate_limit`
- **Description:** Checks the current rate limit status.
- **Documentation Link:** [Rate Limit](https://docs.github.com/en/rest/rate-limit)

---

**Notes:**

- All endpoints require authentication via a Personal Access Token (PAT).
- Be mindful of rate limits and handle them appropriately in your code.
- Use pagination parameters (`per_page`, `page`) to manage large data sets.
