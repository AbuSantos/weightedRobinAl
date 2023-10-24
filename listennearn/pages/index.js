import NFTCard from "../components/contract-card";
import styles from "../styles/Home.module.css";
import {
  listenToEarn_address,
  myToken_address,
  nft_address,
} from "../constants/addresses";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.header}>
          <h1 className={styles.title}>
            Welcome to <span className={styles.gradientText0}>Bullchord</span>
          </h1>
        </div>
        <div className={styles.grid}>
          <NFTCard
            contractAddress={nft_address}
            title="nft music"
            href="/"
            description="This is a test"
          />
        </div>
      </div>
    </main>
  );
}
