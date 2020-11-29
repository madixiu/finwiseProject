import Vue from "vue";
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import VueApollo from "vue-apollo";

const ApolloService = {
  init() {
    const httpLink = new HttpLink({
      // You should use an absolute URL here
      uri: "http://localhost:8000/graphql"
    });

    // Cache implementation graphql/apollo
    const cache = new InMemoryCache();

    // Create the apollo client graphql/apollo
    const apolloClient = new ApolloClient({
      link: httpLink,
      cache
    });
    // using apollo/graphql
    Vue.use(VueApollo);

    const apolloProvider = new VueApollo({
      defaultClient: apolloClient
      // loadingKey to ‘loading’ so that we can easily display a loading indicator in the UI
      // defaultOptions: {
      //   $loadingKey: "loading"
      // }
    });
    return apolloProvider;
  }
};

export default ApolloService;
