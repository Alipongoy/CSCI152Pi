describe('Visit', function() {
    it('Goes to map page, and checks if properly loading', function() {
        cy.visit('localhost:8000')

        cy.contains('LotQ')
        cy.contains('LotS')
        cy.contains('LotP')
        cy.contains('LotJ')
        cy.contains('LotA')
        cy.contains('LotG')
        cy.contains('LotE')
        cy.contains('LotC')
    })
})

describe('Check spots in lotQ', function() {
    it('Clicks on LotQ to see if the spaces render', function() {
        cy.visit('localhost:8000')

        cy.get('[title="LotQ"] > img').click()
        cy.contains('470').click()
        cy.contains('12').click()
        cy.contains('1-1-12')
    })
})

describe('Test Search', function() {
    it('Go to the search landing page and run a search', function() {
        cy.visit('localhost:8000')

        cy.contains('Home').click()
        cy.url().should('include', '/landing.html')

        cy.contains('Map').click()
        cy.get('#inputs').type('Grosse Industrial Tech{downarrow}\n')
    })
})
