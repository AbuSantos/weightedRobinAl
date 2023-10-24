import styles from "../styles/Home.module.css";
import Link from "next/link";
import { ConnectWallet } from "@thirdweb-dev/react";
import { Base } from "@thirdweb-dev/chains";

export default function Navbar() {
  return (
    <div
      className={styles.navbarContainer}
      style={{ cursor: "pointer", fontSize: "1.2rem", fontWeight: "bold" }}
    >
      <Link href="/">
        <p className={styles.gradientText1}>Bullchord Music</p>
      </Link>

      <ConnectWallet
        displayBalanceToken={{
          // 1 is chain id of Ethereum mainnet
          97: "0xFa0EdF5C9DbfD5156a01E6BDc1b220Ca338AD4a2", // contract address of Wrapped BTC token
        }}
      />
    </div>
  );
}
