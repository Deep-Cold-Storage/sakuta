context('Customer Module', () => {
    it('Create a new customer', () => {
      cy.visit('/')
      
      cy.contains('Create Customer').click()
      cy.url().should('include', '/create')
      
      cy.get('[data-cy=name]').type('MageCorp Holdings')
      cy.get('[data-cy=industry]').type('Mining')
      cy.get('[data-cy=nip]').type('6541020129')

      cy.get('.v-list-item__title').contains('Create Customer').click()

      cy.contains('MageCorp Holdings').click()
      cy.url().should('include', '/customers/')

      cy.contains('Delete Customer').click()
    })
  })