<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Assign Contact</h2>
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
              <h4 class="ma-2">Customer's Contacts</h4>
              <p class="ma-2 grey--text">Select which contacts you want to assign to this branch.</p>

              <v-divider></v-divider>
              <v-data-table :headers="contactHeaders" :items="contacts" disable-sort v-bind:loading="isContactsLoading" item-key="name" show-select v-model="selectedContacts">
              </v-data-table>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="assignContacts">
                    <v-list-item-icon><v-icon>mdi-account-plus-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Assign Contact</v-list-item-title></v-list-item-content>
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
    name: "AssignContact",
    data() {
      return {
        customerId: "",
        branch: {},

        selectedContacts: [],
        contacts: [],
        isContactsLoading: true,
        contactHeaders: [
          {
            text: "Contact Name",
            align: "start",
            sortable: false,
            value: "name",
          },
          { text: "E-Mail", value: "email" },
          { text: "Phone", value: "phone" },
        ],
      };
    },
    methods: {
      getContacts() {
        this.$http
          .get("/api/contractors/" + this.branch.contractor_id + "/contacts")
          .then((response) => {
            this.contacts = response.data;
            this.isContactsLoading = false;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getBranch() {
        this.$http
          .get("/api/branches/" + this.branchId)
          .then((response) => {
            this.branch = response.data;

            this.getContacts();
          })
          .catch((error) => {
            console.log(error);
          });
      },

      assignContacts() {
        let isLoopDone = false;

        for (let contact of this.selectedContacts) {
          console.log(contact);

          this.$http
            .post("/api/branches/" + this.branchId + "/contacts/" + contact.contact_id)
            .then(() => {
              if (isLoopDone) {
                this.$router.go(-1);
              }
            })
            .catch((error) => {
              console.log(error);
            });
        }

        isLoopDone = true;
      },
    },
    created() {
      this.branchId = this.$route.params.branchId;

      this.getBranch();
    },
  };
</script>

<style scoped>
  .row-pointer:hover {
    cursor: pointer;
  }
</style>
