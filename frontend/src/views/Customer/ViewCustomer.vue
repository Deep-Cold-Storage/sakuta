<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Customer Details</h2>
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
                        <span class="white--text text-h6">{{ getCustomerInitials(this.customer.name) }}</span>
                      </v-avatar>

                      {{ this.customer.name }}
                    </h2>

                    <v-divider></v-divider>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Customer's NIP </h4> <p> {{ customer.nip }}</p></v-col
                  >
                  <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                    ><h4>Industry </h4> <p> {{ customer.industry }}</p></v-col
                  >
                </v-row>

                <template v-if="customer.pesel || customer.regon">
                  <p class="ma-2 grey--text">Identification Information</p>
                  <v-divider></v-divider>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Customer's Pesel </h4> <p> {{ customer.pesel }}</p></v-col
                    >
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Customer's Regon </h4> <p> {{ customer.regon }}</p></v-col
                    >
                  </v-row>
                </template>

                <template v-if="customer.bank_name || customer.bank_account">
                  <p class="ma-2 grey--text">Bank Information</p>
                  <v-divider></v-divider>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Bank's Name </h4> <p> {{ customer.bank_name }}</p></v-col
                    >
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Account Number </h4> <p> {{ customer.bank_account }}</p></v-col
                    >
                  </v-row>
                </template>

                <template v-if="customer.website || customer.description">
                  <p class="ma-2 grey--text">Other Information</p>
                  <v-divider></v-divider>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Customer's Website </h4> <a color="red accent-3" v-bind:href="customer.website"> {{ customer.website }}</a></v-col
                    >
                  </v-row>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="11" class="ma-2"
                      ><h4>Customer's Description </h4> <p> {{ customer.description }}</p></v-col
                    >
                  </v-row>
                </template>

                <template v-if="invoices">
                  <p class="ma-2 grey--text">Invoices Information</p>
                  <v-divider></v-divider>

                  <v-date-picker v-model="invoicesRange" range no-title></v-date-picker>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="11" class="ma-2"
                      ><h4>All Invoices </h4> <p> {{ invoicesTotal }} Invoices</p></v-col
                    >
                  </v-row>

                  <v-row>
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Paid Balance</h4> <p> {{ balancePaid }} PLN</p></v-col
                    >
                    <v-col xs="12" sm="12" md="12" lg="5" class="ma-2"
                      ><h4>Not Paid Balance </h4> <p> {{ balanceNotPaid }} PLN</p></v-col
                    >
                  </v-row>
                </template>
              </v-container>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Customer's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="editCustomer">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Edit Customer</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item @click="deleteCustomer">
                    <v-list-item-icon><v-icon>mdi-account-cancel-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Delete Customer</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item @click="deleteCustomer">
                    <v-list-item-icon><v-icon>mdi-file-table</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>View Invoices</v-list-item-title></v-list-item-content>
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
              <h4 class="ma-2">Customer's Branches</h4>
              <p class="ma-2 grey--text">Contains all saved branch information for this customer.</p>

              <v-divider></v-divider>
              <v-data-table :headers="branchHeaders" :items="branches" @click:row="handleBranchTableClick" disable-sort class="row-pointer" v-bind:loading="isBranchesLoading">
              </v-data-table>
            </v-sheet>
          </v-col>

          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Branches's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="addBranch">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Add Branch</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>
        </v-row>

        <!-- Third Row -->
        <v-row>
          <v-col lg="2" v-show="$vuetify.breakpoint.mdAndUp"></v-col>

          <v-col xs="12" sm="12" md="12" lg="7">
            <v-sheet rounded class="pa-4">
              <h4 class="ma-2">Customer's Contacts</h4>
              <p class="ma-2 grey--text">Contains all saved contact information for this customer.</p>

              <v-divider></v-divider>
              <v-data-table :headers="contactHeaders" :items="contacts" disable-sort class="row-pointer" v-bind:loading="isContactsLoading" @click:row="handleContactTableClick">
              </v-data-table>
            </v-sheet>
          </v-col>

          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Contact's Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="addContact">
                    <v-list-item-icon><v-icon>mdi-account-edit-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Add Contact</v-list-item-title></v-list-item-content>
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
    name: "View Customers",
    data() {
      return {
        customerId: "",
        customer: {
          name: null,
          industry: null,
          pesel: null,
          regon: null,
          nip: null,
          bank_account: null,
          bank_name: null,
          website: null,
          description: null,
        },

        branches: [],
        isBranchesLoading: true,
        branchHeaders: [
          {
            text: "Branch Name",
            align: "start",
            sortable: false,
            value: "name",
          },
          { text: "Address", value: "address" },
          { text: "City", value: "city" },
          { text: "Postal Code", value: "postal_code" },
          { text: "Country", value: "country" },
        ],

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

        invoices: [],
        invoicesRange: [],
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
            if (error.response.status === 404) {
              this.$router.push("/404");
            }
          });
      },

      getBranches() {
        this.$http
          .get("/api/contractors/" + this.customerId + "/branches")
          .then((response) => {
            this.branches = response.data;
            this.isBranchesLoading = false;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getContacts() {
        this.$http
          .get("/api/contractors/" + this.customerId + "/contacts")
          .then((response) => {
            this.contacts = response.data;
            this.isContactsLoading = false;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getInvoices() {
        this.$http
          // .get("https://not.real/api/" + this.nip + "/invoices", { params: { start: this.invoicesRange[0], stop: this.invoicesRange[1] })
          .get("https://run.mocky.io/v3/900a9c1f-dc40-49e7-bc8e-de0431e15a14", { params: { start: this.invoicesRange[0], stop: this.invoicesRange[1] } })

          .then((response) => {
            this.invoices = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      editCustomer() {
        this.$router.push("/customers/" + this.customerId + "/edit");
      },

      deleteCustomer() {
        this.$http
          .delete("/api/contractors/" + this.customerId)
          .then(() => {
            this.$router.push("/");
          })
          .catch((error) => {
            console.log(error);
          });
      },

      getCustomerInitials(name) {
        try {
          return name
            .split(" ")
            .map(function(item) {
              return item[0];
            })
            .join("")
            .substring(0, 2);
        } catch (error) {
          return "XD";
        }
      },

      handleBranchTableClick(row) {
        this.$router.push("/branches/" + row.branch_id);
      },

      handleContactTableClick(row) {
        this.$router.push("/contacts/" + row.contact_id);
      },

      addBranch() {
        this.$router.push("/customers/" + this.customerId + "/branches");
      },

      addContact() {
        this.$router.push("/customers/" + this.customerId + "/contacts");
      },
    },
    created() {
      this.customerId = this.$route.params.customerId;

      this.getCustomer();
      this.getBranches();
      this.getContacts();
      this.getInvoices();
    },
    computed: {
      balancePaid: function() {
        let paid = 0;

        this.invoices.forEach((invoice) => {
          if (invoice.paid_status) {
            paid += invoice.balance;
          }
        });

        return paid;
      },

      balanceNotPaid: function() {
        let notPaid = 0;

        this.invoices.forEach((invoice) => {
          if (!invoice.paid_status) {
            notPaid += invoice.balance;
          }
        });
        return notPaid;
      },

      invoicesTotal: function() {
        return this.invoices.length;
      },
    },
    watch: {
      invoicesRange: {
        handler() {
          this.getInvoices();
        },
        deep: true,
      },
    },
  };
</script>

<style scoped>
  .row-pointer:hover {
    cursor: pointer;
  }
</style>
