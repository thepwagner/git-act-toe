workflow "play" {
  on = "pull_request"
  resolves = "take turn"
}

action "take turn" {
  uses = "./"
  secrets = ["GITHUB_TOKEN"]
}
