# Git Act Toe

Play Tic Tac Toe with GitHub Actions. Sort of.

This was a quick hack to build "a game" on top of [GitHub Actions](https://github.com/features/actions) for the lulz.
I picked tic-tac-toe because it's simple, and had existing libraries to handle the game logic.

Games happen in GitHub PRs like [this](https://github.com/thepwagner/git-act-toe/pull/4/files).
Each game happens in a unique file. The first line in the file is a serialized copy of the game state, using an HMAC with a key stored as an Actions [Secret](https://developer.github.com/actions/managing-workflows/storing-secrets/) to prevent tampering.
The remainder of the file is a rendered copy of the game board for players to interact with.
As players modify the rendered copy to place their pieces, a GitHub Action monitors the file to enforce the rules - invalid moves are `git revert`-ed.

I thought files were interesting as they keep a public record of move history, and in Git: a hash tree of game results. Blockchain synergy!

This could be extended to a whole league, but I had my lulz and moved on:

* Players would enter by opening a GitHub issue.
* The action would create game PRs and assign two active players.
* When the game has ended, the action merges the PR and updates each player's Issue with win/loss/draw, ELO etc.

