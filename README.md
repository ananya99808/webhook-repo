 Webhook Assignment

This project receives GitHub webhook events (push, pull request, and merge), stores them in MongoDB, and displays them on a simple webpage.

# Webhook

- Webhook endpoint: `/webhook`
- Events handled: `push`, `pull_request`, and `merge`
- Triggered using: [action-repo](https://github.com/ananya99808/action-repo)

## Notes

- Frontend refreshes every 15 seconds to show new events.
- I created **4 pull requests** from the `action-repo` to test that pull request and merge events are received correctly.