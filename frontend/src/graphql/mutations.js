import gql from "graphql-tag";

export const VERIFY_USER = gql`
  mutation verifyAccount($token: String!) {
    verifyAccount(token: $token) {
      success
      errors
    }
  }
`;

//! OLD Register script
// export const REGISTER_USER = gql`
//   mutation register(
//     $username: String!
//     $email: String!
//     $password1: String!
//     $password2: String!
//     $phoneNumber: String!
//     $firstName: String!
//     $lastName: String!
//   ) {
//     register(
//       username: $username
//       email: $email
//       password1: $password1
//       password2: $password2
//       phoneNumber: $phoneNumber
//       firstName: $firstName
//       lastName: $lastName
//     ) {
//       success
//       errors
//     }
//   }
// `;

//? New Register Script
export const REGISTER_USER = gql`
  mutation register(
    $username: String!
    $email: String!
    $password1: String!
    $password2: String!
    $phoneNumber: String!
  ) {
    register(
      username: $username
      email: $email
      password1: $password1
      password2: $password2
      phoneNumber: $phoneNumber
    ) {
      success
      errors
      refreshToken
      token
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

export const UPDATE_USER = gql`
  mutation updateAccount(
    $email: String!
    $username: String!
    $gender: String!
    $degree: String!
    $firstName: String!
    $lastName: String!
    $age: String!
  ) {
    updateAccount(
      email: $email
      username: $username
      gender: $gender
      degree: $degree
      firstName: $firstName
      lastName: $lastName
      age: $age
    ) {
      success
      errors
    }
  }
`;

export const PASS_RESET = gql`
  mutation passwordReset(
    $newPassword1: String!
    $newPassword2: String!
    $token: String!
  ) {
    passwordReset(
      newPassword1: $newPassword1
      newPassword2: $newPassword2
      token: $token
    ) {
      success
      errors
    }
  }
`;

export const PASS_CHANGE = gql`
  mutation passwordChange(
    $oldPassword: String!
    $newPassword1: String!
    $newPassword2: String!
  ) {
    passwordChange(
      oldPassword: $oldPassword
      newPassword1: $newPassword1
      newPassword2: $newPassword2
    ) {
      success
      errors
      token
      refreshToken
    }
  }
`;
