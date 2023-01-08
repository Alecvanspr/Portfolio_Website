import React,{useEffect} from 'react';
import {Container,Col, Row} from 'reactstrap'
import Aboutme from './components/Aboutme';
import CVContainer from './containers/CVContainer'

const CVScene = () => {
    useEffect(()=>{
        const handleScroll = (e) => {
           document.getElementById('blur').style.opacity = 1 - window.scrollY/1000;
        }
        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        }

    },[])
    return (
        <>
        <Aboutme/>
            <Container>
                <CVContainer />
            </Container>
        </>
    )
}
export default CVScene;