/* 
Quick minimal server set up that will allow us to stand up a graphql api
*/

// Require 'apollo-server' 
const { ApolloServer } = require('apollo-server')

// define our schema 
const typeDefs = `
    type Query {
        totalPhotos: Int!
    }
`

/* 
Resolver function to return data for the type
here we are just returning a value of 42
*/
const resolvers = {
    Query: {
        totalPhotos: () => 42
    }
}

/*
Create a new instance of the server.
Send it an object with the schema (typeDefs) and resolvers
*/ 
const server = new ApolloServer({
    typeDefs,
    resolvers
})

// Call listen on the server to launch the web server
server.listen().then(({url}) => console.log(`GraphQL service running on ${url}`))