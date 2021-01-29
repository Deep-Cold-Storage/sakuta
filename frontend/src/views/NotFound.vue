<template>
  <v-app>
    <v-main class="red accent-3">
      <v-container fill-height>
        <v-row justify="center" align="center">
          <v-col cols="12" sm="4" class="error-container">
            <h1>404 - Not Found</h1>
            <h3>The resource you are looking for doesn't exist!</h3>

            <v-btn rounded x-large outlined color="white" class="error-btn" @click="$router.push('/')">
              Go Back Home
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: "NotFound",
  };
</script>

<style scoped>
  .error-container {
    text-align: center;

    color: white;
  }

  .error-container h3 {
    font-weight: 500;
  }

  .error-btn {
    margin-top: 6rem;
    /* font-weight: 600; */
  }
</style>
