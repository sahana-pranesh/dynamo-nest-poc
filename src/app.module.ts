import { Module } from '@nestjs/common';
import { AppController } from './controllers/app.controller';
import { AppService } from './services/app.service';
import { GQLModule } from './modules/graphql.module';
import { ChartResolver } from './resolvers/chart.resolver';
import { ProjectsResolver } from './resolvers/project.resolver';

@Module({
  imports: [GQLModule],
  controllers: [AppController],
  providers: [AppService, ChartResolver, ProjectsResolver],
})
export class AppModule {}
