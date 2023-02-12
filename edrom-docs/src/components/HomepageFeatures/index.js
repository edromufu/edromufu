import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Robôs',
    Svg: require('@site/static/img/robot-generic.svg').default,
    description: (
      <>
        Dedicada a criação de robês de competição, estudamos e pesquisamos muito para criarmos o melhor robô possivel do zero.
      </>
    ),
  },
  {
    title: 'EDROM',
    Svg: require('@site/static/img/logo-edrom.svg').default,
    description: (
      <>
        Equipe de extensão da Universidade Federal de Uberlândia.
      </>
    ),
  },
  {
    title: 'Documentação',
    Svg: require('@site/static/img/brain-generic.svg').default,
    description: (
      <>
        Site dedicado a documentação das área de equipe, com explicação sobre códigos, execução e ferramentas utilizadas.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
