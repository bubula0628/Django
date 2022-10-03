<template>

  <div id="grid">
      <div id="Register">
          <h3>Register</h3>
          <form>
              <div class="form-elem">
                  <span>Username : </span>
                  <input v-model="registerName" type="text" placeholder="username">
              </div>

              <div class="form-elem">
                  <span>Password : </span>
                  <input v-model="registerPwd" type="password" placeholder="password">
              </div>

              <div class="form-elem">
                  <button v-on:click.prevent="register">Submit</button>
              </div>
          </form>
      </div>

      <div id="Login">
          <h3>Login</h3>
          <form>
              <div class="form-elem">
                  <span>Username : </span>
                  <input v-model="loginName" type="text" placeholder="username">
              </div>

              <div class="form-elem">
                  <span>Password : </span>
                  <input v-model="loginPwd" type="password" placeholder="password">
              </div>

              <div class="form-elem">
                  <button v-on:click.prevent="login">Login</button>
              </div>
          </form>
      </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
      name: 'Login',

      data: function () {
          return {
              registerName: '',
              registerPwd: '',
              loginName: '',
              loginPwd: '',
              signupResponse: null,
          }
      },
      methods: {
          register() {
              const that = this;
              axios.post('http://127.0.0.1:8000/api/user/', {
                      username: this.registerName,
                      password: this.registerPwd,
                  })
                  .then(function (response) {
                      that.signupResponse = response.data;
                      alert('Register Success! Go to Login!');
                  })
                  .catch(function (error) {
                      alert(error.message);
                  });
          },
          login() {
              const that = this;
              axios.post('http://127.0.0.1:8000/api/token/', {
                      username: that.loginName,
                      password: that.loginPwd,
                  })
                  .then(function (response) {
                      const storage = localStorage;
                      const expiredTime = Date.parse(response.headers.date) + 60 * 100 * 1000;
                      // localStorage
                      storage.setItem('access.login', response.data.access);
                      storage.setItem('refresh.login', response.data.refresh);
                      storage.setItem('expiredTime.login', expiredTime);
                      storage.setItem('username.login', that.loginName);
                      // superuser
                      axios.get('http://127.0.0.1:8000/api/user/' + that.loginName + '/')
                          .then(function (response) {
                              storage.setItem('isSuperuser.login', response.data.is_superuser);
                              // router
                              that.$router.push({name: 'About'});
                          });
                          // .catch(...)
                  })
                  .catch(function () {
                      alert("We don't know you!");
                  });
              }
      }
  }
</script>

<style scoped>
  #grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
  }
  #signup {
      text-align: center;
  }
  #signin {
      text-align: center;
  }
  .form-elem {
      padding: 10px;
  }
  input {
      height: 25px;
      padding-left: 10px;
  }
  button {
      height: 35px;
      cursor: pointer;
      border: none;
      outline: none;
      background: gray;
      color: whitesmoke;
      border-radius: 5px;
      width: 60px;
  }
</style>