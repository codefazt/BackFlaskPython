# Task: Typeahead Backend

## Description

Typeahead or autocomplete is a common feature that people come across on websites. For example, when you are searching on Google, you will notice a word populates before you finish typing.

For example, if the data provided is `{ "John": 21, "James": 43, "Joanna": 13, "Ja": 3 }` and a user queries `j`, then it returns `[{ "name": "James", "times": 43 }, { "name": "John", "times": 21 }, { "name": "Joanna", "times": 13 }, { "name": "Ja", "times": 3 }]`. Note, the search is case-insensitive.

In addition, an exact match would take precedence despite of the popularity. For example, a search keyword `ja` would return `[{ "name": "Ja", "times": 3 }, { "name": "James", "times": 43 }]` since `Ja` has an exact match.

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


Have fun!