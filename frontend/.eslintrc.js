module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ["plugin:vue/essential", "@vue/prettier"],
  rules: {
    "no-console": "off",
    "no-debugger": "off",
    "max-len": ["error", { "code": 360 }]
  },
  parserOptions: {
    parser: "babel-eslint"
  }
};
