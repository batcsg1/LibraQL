<div align="center">
  <img height="296" alt="image" src="./assets/logo.png" />
</div>

# Disclaimer

- ⚠️ The project is under very active development.
- ⚠️ Expect bugs and breaking changes.

# About the Project

## Database Storage:
### Bye Bye JSON...
There are many No-SQL DBMS's out there, in particular document DBMS's such as **MongoDB**, **CouchDB** and **RavenDB**. All of these DBMS's store data in a JSON-like format. Now if you're wondering what heck [JSON](https://en.wikipedia.org/wiki/JSON) is all about, it is simply a very popular data format that is primarly used by web applications. It is short for (_*JavaScript Object Notation*_).

The problem with **JSON** however, is that is not a particularly token efficent format, in laymans term's meaning there are many redundant characters such as brackets `[]`, braces `{}`, quotes: `""` and commas `,`. This inflated amount o tokens can get very hard to read for tools like DBMS's to process, particularly when reading through large datasets.

### Hello TOON...
However LibraQL utilizes a new revolutionary format called **TOON** _(Token-Oriented Object Notation)_ for its database storage. 

### Visuals of why TOON is better
**JSON** vs **TOON** objects containing 2 users:
**JSON**: _12 lines of code_
```json
"users": [
    {
        "id": 1,
        "name": "Alice",
        "role": "admin"
    },
    {
        "id": 2,
        "name": "Bob",
        "role": "user"
    }
]
```
**JSON**: **_only 3 lines of code!!_**

```toon
users: id,name,role
1,Alice,admin
2,Bob,user   
```
As you can see, TOON takes up way less lines compared to an equivalent JSON object with equivalent data. Anyways,enough about my rant about TOON, here is some more stuff about TOON linked down below:


[More about TOON and it's usage for LLM's](https://medium.com/@jenilsojitra/the-complete-beginners-guide-to-toon-format-token-oriented-object-notation-957e8cf14590)

## Data Access





---
<div align="center">
  <img src="https://raw.githubusercontent.com/batcsg1/batcsg1/refs/heads/main/Logo.png" height="60" alt="SB-Logo">

  **Copyleft 🄯 2026 Samuel Batchelor**
  
  [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://github.com/batcsg1/LibraQL/blob/main/LICENSE)

  *Freely distributable and modifiable under the [GNU AGPL v3.0](https://github.com/batcsg1/LibraQL/blob/main/LICENSE).*
</div>
