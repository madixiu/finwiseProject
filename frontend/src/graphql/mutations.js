import gql from 'graphql-tag'

export const REGISTER_USER = gql`
mutation register($email: String! $username: String! $password1: String! $password2: String! 
    $firstName: String! $lastName: String!
    $phoneNumber: String! $gender: String! 
    $degree: String! $birth: String!)

`