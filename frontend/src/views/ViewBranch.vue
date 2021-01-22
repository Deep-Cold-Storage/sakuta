<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Branch Detail</h2>
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
          <v-col cols="12" xs="12" sm="12" md="12" lg="7">
            <v-sheet rounded>
              <v-container>
                <v-row>
                  <v-col>
                    <h2 class="ma-2">
                      <v-avatar size="50" class="ma-3" color="red accent-3" v-if="$vuetify.breakpoint.lgAndUp">
                        <span class="white--text text-h6">{{ getBranchInitials(this.branch.name) }}</span>
                      </v-avatar>

                      {{ this.branch.name }}
                    </h2>

                    <v-divider></v-divider>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Address </h4> <p> {{ branch.address }}</p></v-col
                  >
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>City </h4> <p> {{ branch.city }}</p></v-col
                  >
                </v-row>

                <v-row>
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Postal Code </h4> <p> {{ branch.postal_code }}</p></v-col
                  >
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Country </h4> <p> {{ branch.country }}</p></v-col
                  >
                </v-row>
              </v-container>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Branch's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="editBranch">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Edit Branch</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item @click="deleteBranch">
                    <v-list-item-icon><v-icon>mdi-account-cancel-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Delete Branch</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>
        </v-row>

        <!-- Second Row -->
        <v-row>
          <v-col lg="2" v-show="$vuetify.breakpoint.mdAndUp"></v-col>

          <v-col xs="12" sm="12" md="12" lg="7">
            <v-sheet rounded class="pa-4">
              <h4 class="ma-2">Assigned Contacts</h4>
              <p class="ma-2 grey--text">Contains all assigned contacts to this branch.</p>

              <v-divider></v-divider>
              <v-data-table :headers="contactHeaders" :items="contacts" disable-sort v-bind:loading="isContactsLoading">
                <template v-slot:[`item.actions`]="{ item }">
                  <v-icon small @click="deleteContact(item)" class="mr-2">
                    mdi-delete
                  </v-icon>

                  <v-icon small @click="$router.push('/contacts/' + item.contact_id)">
                    mdi-card-account-details
                  </v-icon>
                </template>
              </v-data-table>
            </v-sheet>
          </v-col>

          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Contacts's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="assignContact">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Assign Contact</v-list-item-title></v-list-item-content>
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
    name: "ViewBranch",
    data() {
      return {
        branchId: "",
        branch: {},

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
          { text: "Actions", value: "actions", sortable: false, align: "center" },
        ],
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

      editBranch() {
        this.$router.push("/branches/" + this.branchId + "/edit");
      },

      deleteBranch() {
        this.$http
          .delete("/api/branches/" + this.branchId)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getBranchInitials(name) {
        return name
          .split(" ")
          .map(function(item) {
            return item[0];
          })
          .join("")
          .substring(0, 2);
      },

      getContacts() {
        this.$http
          .get("/api/branches/" + this.branchId + "/contacts")
          .then((response) => {
            this.contacts = response.data;
            this.isContactsLoading = false;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      deleteContact(contact) {
        this.$http
          .delete("/api/branches/" + this.branchId + "/contacts/" + contact.contact_id)
          .then(() => {
            this.getContacts();
          })
          .catch((error) => {
            console.log(error);
          });
      },

      handleContactTableClick(row) {
        this.$router.push("/contacts/" + row.contact_id);
      },

      assignContact() {
        this.$router.push("/branches/" + this.branchId + "/contacts");
      },
    },
    created() {
      this.branchId = this.$route.params.branchId;

      this.getBranch();
      this.getContacts();
    },
  };
</script>
