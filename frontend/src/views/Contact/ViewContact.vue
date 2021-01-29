<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Contact Detail</h2>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-4">
      <v-container>
        <!-- First Row -->
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
            <v-sheet rounded>
              <v-container>
                <v-row>
                  <v-col>
                    <h2 class="ma-2">
                      <v-avatar size="50" class="ma-3" color="red accent-3" v-show="$vuetify.breakpoint.lgAndUp">
                        <span class="white--text text-h6">{{ getContactInitials(this.contact.name) }}</span>
                      </v-avatar>

                      {{ this.contact.name }}
                    </h2>

                    <v-divider></v-divider>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>E-Mail </h4> <p> {{ contact.email }}</p></v-col
                  >
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Phone </h4> <p> {{ contact.phone }}</p></v-col
                  >
                </v-row>

                <v-row v-if="contact.description">
                  <v-col xs="12" sm="12" md="12" lg="11" class="ma-2"
                    ><h4>Description </h4> <p> {{ contact.description }}</p></v-col
                  >
                </v-row>
              </v-container>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Contact's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="editContact">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Edit Contact</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item @click="deleteContact">
                    <v-list-item-icon><v-icon>mdi-account-cancel-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Delete Contact</v-list-item-title></v-list-item-content>
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
    name: "View Contact",
    data() {
      return {
        contactId: "",
        contact: {},
      };
    },
    methods: {
      getContact() {
        this.$http
          .get("/api/contacts/" + this.contactId)
          .then((response) => {
            this.contact = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      editContact() {
        this.$router.push("/contacts/" + this.contactId + "/edit");
      },

      deleteContact() {
        this.$http
          .delete("/api/contacts/" + this.contactId)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getContactInitials(name) {
        return name
          .split(" ")
          .map(function(item) {
            return item[0];
          })
          .join("")
          .substring(0, 2);
      },
    },
    created() {
      this.contactId = this.$route.params.contactId;

      this.getContact();
    },
  };
</script>
