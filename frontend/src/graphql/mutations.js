import gql from "graphql-tag";
export const VERIFY_USER = gql`
  mutation verifyToken($token: String!) {
    verifyToken(token: $token) {
      success
      errors
      payload
    }
  }
`;
// export const VERIFY_USER = gql`
//   {
//     verifyToken(token: String!) {

//         success
//         errors
//         payload

//     }
//   }
// `;

export const REGISTER_USER = gql`
  mutation register(
    $username: String!
    $email: String!
    $password1: String!
    $password2: String!
    $phoneNumber: String!
    $firstName: String!
    $lastName: String!
  ) {
    register(
      username: $username
      email: $email
      password1: $password1
      password2: $password2
      phoneNumber: $phoneNumber
      firstName: $firstName
      lastName: $lastName
    ) {
      success
      errors
    }
  }
`;

export const LOGIN_USER = gql`
  mutation tokenAuth($phoneNumber: String!, $password: String!) {
    tokenAuth(phoneNumber: $phoneNumber, password: $password) {
      success
      errors
      unarchiving
      token
      refreshToken

      user {
        id
        username
      }
    }
  }
`;
