import { Composition, Folder } from "remotion";
import { MyComposition } from "./MyComposition";
import { GorgiasCounter } from "./GorgiasCounter";
import { GorgiasUnifiedInbox } from "./GorgiasUnifiedInbox";
import { ShowcaseVideo } from "./ShowcaseVideo";
import "./style.css";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Folder name="Gorgias">
        <Composition
          id="GorgiasCounter"
          component={GorgiasCounter}
          durationInFrames={150}
          fps={30}
          width={1920}
          height={1080}
        />
        <Composition
          id="GorgiasUnifiedInbox"
          component={GorgiasUnifiedInbox}
          durationInFrames={150}
          fps={30}
          width={1920}
          height={1080}
        />
      </Folder>
      <Composition
        id="MyComposition"
        component={MyComposition}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="ShowcaseVideo"
        component={ShowcaseVideo}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
