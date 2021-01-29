<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Edit Customer</h2>
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
                <p class="ma-2 grey--text" v-show="$vuetify.breakpoint.mdAndUp">(Optional) - Information such as name and NIP.</p>
                <v-divider></v-divider>
                <v-text-field class="ma-2" flat hide-details label="Customer Name" outlined v-model="customer.name"></v-text-field>

                <v-row dense>
                  <v-col xs="12" sm="12" md="12" lg="6"><v-text-field class="ma-2" flat hide-details label="Industry" outlined v-model="customer.industry"></v-text-field></v-col>
                  <v-col xs="12" sm="12" md="12" lg="6"><v-text-field class="ma-2" flat hide-details label="NIP" outlined v-model="customer.nip"></v-text-field></v-col>
                </v-row>

                <br />
                <h4 class="ma-2">Identification Information</h4>
                <p class="ma-2 grey--text" v-show="$vuetify.breakpoint.mdAndUp">(Optional) - Information such as PESEL and REGON.</p>
                <v-divider></v-divider>
                <v-row dense>
                  <v-col><v-text-field class="ma-2" flat hide-details label="Pesel" outlined v-model="customer.pesel"></v-text-field></v-col>
                  <v-col><v-text-field class="ma-2" flat hide-details label="Regon" outlined v-model="customer.regon"></v-text-field></v-col>
                </v-row>

                <br />
                <h4 class="ma-2">Bank Information</h4>
                <p class="ma-2 grey--text" v-show="$vuetify.breakpoint.mdAndUp">(Optional) - Information such as bank name and account number.</p>
                <v-divider></v-divider>

                <v-row dense>
                  <v-col><v-text-field class="ma-2" flat hide-details label="Bank Name" outlined v-model="customer.bank_name"></v-text-field></v-col>
                  <v-col><v-text-field class="ma-2" flat hide-details label="Account Number" outlined v-model="customer.bank_account"></v-text-field></v-col>
                </v-row>

                <br />
                <h4 class="ma-2">Other Information</h4>
                <p class="ma-2 grey--text" v-show="$vuetify.breakpoint.mdAndUp">(Optional) - Information such as website and notes.</p>
                <v-divider></v-divider>

                <v-text-field class="ma-2" flat hide-details label="Website" outlined v-model="customer.website"></v-text-field>
                <v-textarea class="ma-2" flat hide-details label="Description" outlined v-model="customer.description"></v-textarea>
              </v-container>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="updateCustomer">
                    <v-list-item-icon><v-icon>mdi-account-plus-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Update Customer</v-list-item-title></v-list-item-content>
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
    name: "CreateCustomers",
    data() {
      return {
        customer: {},

        headers: [
          {
            text: "Customer Name",
            align: "start",
            sortable: false,
            value: "name",
          },
          { text: "Industry", value: "industry" },
          { text: "Website", value: "website" },
          { text: "NIP", value: "nip" },
        ],
      };
    },
    methods: {
      getCustomer() {
        this.$http
          .get("/api/contractors/" + this.customerId)
          .then((response) => {
            this.customer = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      updateCustomer() {
        this.$http
          .put("/api/contractors/" + this.customerId, this.customer)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    created() {
      this.customerId = this.$route.params.customerId;

      this.getCustomer();
    },
  };
</script>

<style scoped>
  .row-pointer:hover {
    cursor: pointer;
  }
</style>
