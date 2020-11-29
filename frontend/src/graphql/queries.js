import gql from "graphql-tag";

export const GET_USER = gql`
  query {
    me {
      id
      username
      email
      lastName
      firstName
      phoneNumber
      expirationDate
      role
      isStaff
      isActive
      verified
    }
  }
`;

//dummy, delete soon
export const USER = gql`
  query {
    users(username: "09386886616") {
      edges {
        node {
          id
          username
          firstName
          email
          degree
          isActive
          archived
          verified
          secondaryEmail
        }
      }
    }
  }
`;
