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
    })
    
    it('Create a new branch', () => {
      cy.contains('Add Branch').click()
      
      cy.get('[data-cy=name]').type('MageCorp Branch')
      cy.get('[data-cy=address]').type('Mining Street')
      cy.get('[data-cy=postal_code]').type('45-550')
      cy.get('[data-cy=country]').type('Poland')
      cy.get('[data-cy=city]').type('Magicka')

      cy.get('.v-list-item__title').contains('Create Branch').click()

      cy.contains('MageCorp Branch').click()
      cy.url().should('include', '/branches/')
        
      cy.contains('Delete Branch').click()
    })

    it('Create a new contact', () => {
      cy.contains('Add Contact').click()
      
      cy.get('[data-cy=name]').type('Jerzy Baranowski')
      cy.get('[data-cy=email]').type('jbaran@gmail.com')

      cy.get('.v-list-item__title').contains('Create Contact').click()

      cy.contains('Jerzy Baranowski').click()
      cy.url().should('include', '/contacts/')
        
      cy.contains('Delete Contact').click()
    })

    it('Delete customer', () => {
      cy.contains('Delete Customer').click()
    })

  })
     