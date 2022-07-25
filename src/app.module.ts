import { Module } from '@nestjs/common';
import { AppController } from './controllers/app.controller';
import { AppService } from './app.service';
import { GQLModule } from './modules/graphql.module';
import { ChartResolver } from './resolvers/chart.resolver';

@Module({
  imports: [GQLModule],
  controllers: [AppController],
  providers: [AppService, ChartResolver],
})
export class AppModule {}
