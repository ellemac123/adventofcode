## Graphql with Javascript and Apollo Server

We'll be following on from the O'Reilly Tutorial in Learning GraphQL by Eve Porcello, Chapter Five.

In this tutorial we built out a Photo Share App which use Javascript and use Apollo for our GraphQL server.


To start, install our packages and run the server.

```bash
npm install
npm start
```

This will run our GraphQL Playground on `localhost:4000/`

You can hit the totalPhotos query with either

```graphql
query totalPhotos {
  totalPhotos
}
```

or 

```graphql
{totalPhotos}
```
