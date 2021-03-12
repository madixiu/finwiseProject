import gql from "graphql-tag";

// export const GET_USER = gql`
//   query {
//     me {
//       id
//       username
//       email
//       lastName
//       firstName
//       phoneNumber
//       expirationDate
//       role
//       isStaff
//       isActive
//       verified
//     }
//   }
// `;
export const GET_USER = gql`
  query users($username: String!) {
    users(username: $username) {
      edges {
        node {
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
          age
          degree
        }
      }
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
