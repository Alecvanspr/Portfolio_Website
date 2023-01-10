import React from "react";
import { Container, Row } from "reactstrap";
import NavButton from "../../shared/components/NavButton";
import './Header.css';

const Header = () => {
    return(
        <>
        <div className="nav-group">
        <Container>
            <Row>
            <p className="h2">Alec van Spronsen</p>
                <div>
                    <NavButton 
                        label="knop 1"
                    />
                    <NavButton 
                        label="knop 2"
                    />
                    <NavButton 
                        label="knop 3"
                    />
                    </div>
                </Row>
                </Container>
            </div>
        </>
    )
}
export default Header;