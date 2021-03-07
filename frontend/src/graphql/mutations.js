import gql from "graphql-tag";

export const VERIFY_USER = gql`
  mutation verifyAccount($token: String!) {
    verifyAccount(token: $token) {
      success
      errors
    }
  }
`;

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

// export const LOGIN_USER = gql`
//   mutation tokenAuth($phoneNumber: String!, $password: String!) {
//     tokenAuth(phoneNumber: $phoneNumber, password: $password) {
//       success
//       errors
//       unarchiving
//       token
//       refreshToken

//       user {
//         id
//         username
//       }
//     }
//   }
// `;

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
  }
`;
export const VERIFY_ACCESS_TOKEN = gql`
  mutation verifyToken($token: String!) {
    verifyToken(token: $token) {
      success
      errors
      payload
    }
  }
`;

export const REFRESH_ACCESS_TOKEN = gql`
  mutation refreshToken($refreshToken: String!) {
    refreshToken(refreshToken: $refreshToken) {
      success
      errors
      token
      payload
    }
  }
`;

export const REVOKE_TOKEN = gql`
  mutation revokeToken($refreshToken: String!) {
    revokeToken(refreshToken: $refreshToken) {
      revoked
    }
  }
`;

// export const UPDATE_USER = gql`
// mutation updateAccount($email: String!,)`;
