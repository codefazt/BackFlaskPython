# Task: Typeahead Backend

## Description

Typeahead or autocomplete is a common feature that people come across on websites. For example, when you are searching on Google, you will notice a word populates before you finish typing.

For this task, you'll implement the backend of a simple typeahead system. You will be provided with a list of names and their popularities.

You're asked to write up a typeahead backend system **using a prefix tree** ordered by popularity. You should not use a database to implement your solution.

For example, if the data provided is `{ "John": 21, "James": 43, "Joanna": 13, "Ja": 3 }` and a user queries `j`, then it returns `[{ "name": "James", "times": 43 }, { "name": "John", "times": 21 }, { "name": "Joanna", "times": 13 }, { "name": "Ja", "times": 3 }]`. Note, the search is case-insensitive.

In addition, an exact match would take precedence despite of the popularity. For example, a search keyword `ja` would return `[{ "name": "Ja", "times": 3 }, { "name": "James", "times": 43 }]` since `Ja` has an exact match.

## Specific requirements

When running your app you will have three environment variables available:

- `PORT`: your app must receive requests using this port
- `SUGGESTION_NUMBER`: this will be the max amount of results for the `GET` endpoint
- `HOST`: the host that will be used to refer to your running app. Requests will not be to `http://localhost:{PORT}` as you probably do when running locally, they will be to `http:some-host:{PORT}`. Some frameworks have, by default, a list of allowed hosts, so any request going to a host not listed there will get blocked. If that's your case, you need to either add the host present in this environment variable to your framework's allowed hosts configuration (not all of them need this: Express doesn't, Rails and Django do) or disable this allowed hosts block (not recommended for real projects)

All endpoints in this **REST API** will return and receive (when it applies) JSON.

It's not a requirement to have persistency across application restarts, but while running, the application must behave as if it has persistency when queried to modify data (i.e. if you send a request to modify a name, and then you query that name, the app must return the modified name).

The initial data is on the `names.json` file in this repository, in the format `{ [name1]: [popularityOfName1], [name2]: [popularityOfName2], ... }`. **It is extremely important that you don't change this file, as automated tests will assume this exact file as the initial data for your application**.

You will need to write two endpoints of this REST API to approve this task:

### `GET /typeahead/{prefix}`

It receives a prefix in the path and returns an array of objects each one having the `name` and `times` attributes. The result contains all the names that have the given `prefix` up to a maximum of `SUGGESTION_NUMBER` names, sorted by highest popularity (`times`) – and name in ascending order if they have equal popularity – always leaving the exact match at the beginning, if there is one (see examples in general description).

If the `prefix` portion of the request is not given or empty, it returns the `SUGGESTION_NUMBER` names with highest popularity (and sorted by name ascending in case of equal popularity).

This endpoint must be case insensitive, as per the initial description.

#### Example

```bash
$ curl -X GET http://host:port/typeahead/ja

[{"name":"Janetta","times":973},{"name":"Janel","times":955},{"name":"Jazmin","times":951},{"name":"Janette","times":947},{"name":"Janet","times":936},{"name":"Janeva","times":929},{"name":"Janella","times":916},{"name":"Janeczka","times":915},{"name":"Jaquelin","times":889},{"name":"Janaya","times":878}]
```

### `POST /typeahead`

It receives a JSON object with a name as the request body (example: `{ "name": "Joanna" }`), increases the popularity for that name in 1, and returns a `201` status code with an object with `name` and `times` properties considering the new state.

If the given name does not exist in the data (`names.json`) then this endpoint should return a 400 HTTP error (so no new names will be added, it will only increase popularity on existing names).

This endpoint must be case insensitive, as per the initial description.

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Joanna"}' http://localhost:8080/typeahead

{"name":"Joanna","times":441}
```

## How to work on the task

### Before you start

First, you need to choose a stack to work on this task. Our advice is you should choose a stack you feel comfortable with, so you not only solve this, but also do it with good quality code that properly shows your skills. The only requirement is to have a `Dockerfile` that can run your app (assuming Docker running on Linux), since our automated tests will need this. This base comes with a working `Dockerfile` for a Node.js app with an `index.js` main file, but feel free to change this to adapt it to your stack. See [here](https://github.com/matilda-applicants/common-tasks-instructions/wiki/Docker-on-your-task) for more details on this Dockerfile and examples for other stacks in case you are not familiar with Docker (knowing Docker is not a requirement for this task; if you have trouble with it feel free to reach out to us).

Don't forget to change the `.gitignore` file in this repository to the one you use for your stack. The initial one on this repository should cover all the common ignores for Node.js stacks, so adapt it to the one you chose. This is important so you avoid uploading to your repository all your dependencies, logs and such.

### Automated tests

Whenever you push commits to the `master` branch, you will trigger our automated tests. See [here](https://github.com/matilda-applicants/common-tasks-instructions/wiki/Automatic-task-validation) for details on how to check the automated tests results and see useful logs in case of a failure.

The `master` branch is thus special. These automated tests are not meant to do TDD; you can do TDD if you want, but with your own tests :). You should treat pushes to `master` as you would treat production deployments. If the automated tests fail, it's like a production bug, and the logs covered in red are your users' complaints. You don't want that, do you? Feel free to use any other branch on this repository, as well as the pull requests and issues if you need to. Just be mindful about `master`.

### Submitting your task

Before you submit your task, you need to make sure the tests on your `master` branch's latest commit (HEAD) are successful. The submission will be just that: the latest commit on `master`. So when you are ready, just let us know and we'll proceed with the human revision.

## Evaluation

From the previous explanation you know there are automated tests and a human revision once those automated tests pass. The evaluation criteria for the automated tests is simple: be green. Tests cover a large amount of cases, so being green ensures the correctness of your solution.

As for the human revision, the actual result will not only depend on what you submitted, but also on the level of seniority we expect from you (taken from your application to the job). But in general, the human revision is focused on:

- **good code**: what does this mean exactly? we want to learn what it means to you by looking at the code you write
- **performant code**: we won't expect the most performant solution possible, but we do expect you to be mindful about performance. You can tell that from the code you write
- **good solution**: although this is a fictitious and fairly short task, we expect you implement it as you would in a real job; don't focus on showcasing specific skills or knowledge, focus on showcasing what a great engineer you can be for a real company

Have fun!