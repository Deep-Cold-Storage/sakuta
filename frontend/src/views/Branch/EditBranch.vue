<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Edit Branch</h2>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-4">
      <v-container>
        <v-row>
          <!-- Navigation -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list shaped rounded>
                <v-subheader>Navigation</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="$router.go(-1)">
                    <v-list-item-icon><v-icon>mdi-backburger</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Go Back</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>

          <!-- Main Summary -->
          <v-col xs="12" sm="12" md="12" lg="7">
            <v-sheet rounded class="pa-4">
              <v-container>
                <h4 class="ma-2">Basic Information</h4>
                <p class="ma-2 grey--text" v-show="$vuetify.breakpoint.mdAndUp">(Optional) - Information such as name and address information.</p>
                <v-divider></v-divider>
                <v-text-field class="ma-2" flat hide-details label="Name" outlined v-model="branch.name"></v-text-field>

                <v-row dense>
                  <v-col xs="12" sm="12" md="12" lg="6"><v-text-field class="ma-2" flat hide-details label="Address" outlined v-model="branch.address"></v-text-field></v-col>
                  <v-col xs="12" sm="12" md="12" lg="6"><v-text-field class="ma-2" flat hide-details label="City" outlined v-model="branch.city"></v-text-field></v-col>
                </v-row>

                <v-row dense>
                  <v-col xs="12" sm="12" md="12" lg="6"
                    ><v-text-field class="ma-2" flat hide-details label="Postal Code" outlined v-model="branch.postal_code"></v-text-field
                  ></v-col>
                  <v-col xs="12" sm="12" md="12" lg="6"><v-text-field class="ma-2" flat hide-details label="Country" outlined v-model="branch.country"></v-text-field></v-col>
                </v-row>
              </v-container>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="updateBranch">
                    <v-list-item-icon><v-icon>mdi-account-plus-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Edit Branch</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item @click="$router.go(-1)">
                    <v-list-item-icon><v-icon>mdi-account-cancel-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Cancel</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: "EditBranch",
    data() {
      return {
        branch: {},
        branchId: "",
      };
    },
    methods: {
      getBranch() {
        this.$http
          .get("/api/branches/" + this.branchId)
          .then((response) => {
            this.branch = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      updateBranch() {
        this.$http
          .put("/api/branches/" + this.branchId, this.branch)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    created() {
      this.branchId = this.$route.params.branchId;

      this.getBranch();
    },
  };
</script>
