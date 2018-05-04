describe('My First Test', function() {
    it('Does not do much!', function() {
        expect(true).to.equal(true)
    })
})
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
        cy.contains('LotY')

    })
})

describe('Check spots in lotQ', function() {
    it('Clicks on LotQ to see if the spaces render', function() {
        cy.visit('localhost:8000')
        cy.get('.title')

        cy.get('[title="LotQ"] > img').click()
        cy.contains('470').click()
        cy.contains('12').click()
        cy.contains('1-1-12')
    })
})
